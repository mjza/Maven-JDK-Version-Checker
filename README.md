# Description
A python application for detecting the JDK version of a given Maven artificat.

# Setup 

## Install Maven

```bash
brew install maven
```

## Creating the Virtual Environment
First, navigate to your project's root directory in your terminal. Then, create a virtual environment named venv (or another name of your choice) by running:

```bash
python3 -m venv venv
```

This command creates a new directory named venv in your project directory, which contains a copy of the Python interpreter, the standard library, and various supporting files.

## Activating the Virtual Environment
Before you can start installing packages, you need to activate the virtual environment. 
Activation will ensure that the Python interpreter and tools within the virtual environment are used in preference to the system-wide Python installation.

1. **On macOS and Linux:**

```
source venv/bin/activate
```

2. **On Windows (cmd.exe):**

```
.\venv\Scripts\activate.bat
```

3. **On Windows (PowerShell) or VSC Terminal:**

```
.\venv\Scripts\Activate.ps1
```

Once activated, your terminal prompt must change to indicate that the virtual environment is active.

## Installing Dependencies

If you want to install all requirements at once use the following instruction with the virtual environment activated:

```bash
pip install -r requirements.txt
```

Otherwise follow the next section for installing required libraries step by step.

# Example usage
```bash
python3 check_java_version.py \
  --groupId jakarta.servlet.jsp.jstl \
  --artifactId jakarta.servlet.jsp.jstl-api \
  --version 2.0.0
```