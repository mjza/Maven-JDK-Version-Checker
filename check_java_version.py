import os
import subprocess
import zipfile
import tempfile
import argparse

def get_maven_artifact(group_id, artifact_id, version):
    artifact_str = f"{group_id}:{artifact_id}:{version}"
    print(f"Downloading {artifact_str}...")
    subprocess.run(["mvn", "dependency:get", f"-Dartifact={artifact_str}"], check=True)
    
    local_repo = os.path.expanduser("~/.m2/repository")
    artifact_path = os.path.join(local_repo, group_id.replace(".", "/"), artifact_id, version, f"{artifact_id}-{version}.jar")
    
    if not os.path.isfile(artifact_path):
        raise FileNotFoundError(f"Artifact not found at: {artifact_path}")
    
    return artifact_path

def extract_jar_and_get_major_versions(jar_path):
    with tempfile.TemporaryDirectory() as tmpdir:
        with zipfile.ZipFile(jar_path, 'r') as zip_ref:
            zip_ref.extractall(tmpdir)

        major_versions = set()
        for root, _, files in os.walk(tmpdir):
            for file in files:
                if file.endswith(".class"):
                    class_file = os.path.join(root, file)
                    try:
                        with open(class_file, 'rb') as f:
                            f.read(6)  # skip magic + minor version
                            major = int.from_bytes(f.read(2), byteorder='big')
                            major_versions.add(major)
                    except Exception as e:
                        print(f"Error reading {file}: {e}")
        return major_versions

def java_version_from_major(major):
    mapping = {
        52: "Java 8",
        53: "Java 9",
        54: "Java 10",
        55: "Java 11",
        56: "Java 12",
        57: "Java 13",
        58: "Java 14",
        59: "Java 15",
        60: "Java 16",
        61: "Java 17",
        62: "Java 18",
        63: "Java 19",
        64: "Java 20",
    }
    return mapping.get(major, f"Unknown (major version {major})")

def main():
    parser = argparse.ArgumentParser(description="Check Java compatibility of a Maven artifact.")
    parser.add_argument('--groupId', required=True, help='Group ID of the artifact')
    parser.add_argument('--artifactId', required=True, help='Artifact ID of the artifact')
    parser.add_argument('--version', required=True, help='Version of the artifact')

    args = parser.parse_args()

    try:
        jar_path = get_maven_artifact(args.groupId, args.artifactId, args.version)
        major_versions = extract_jar_and_get_major_versions(jar_path)

        print("\nDetected major versions in JAR:")
        for major in sorted(major_versions):
            print(f"  - {major} → {java_version_from_major(major)}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
