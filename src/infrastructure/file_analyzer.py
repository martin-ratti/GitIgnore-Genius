# src/infrastructure/file_analyzer.py

import os
import platform
from typing import List, Dict, Callable

# Define a type for our detection rules for clarity
DetectionRule = Callable[[str], bool]

# Define the "fingerprints" for each technology.
# Each key is the technology name (must match the template filename).
# Each value is a function that returns True if the technology is detected.
DETECTION_RULES: Dict[str, DetectionRule] = {
    # Languages & Frameworks
    "Python": lambda path: any(f.endswith('.py') for f in os.listdir(path)) or \
                           os.path.exists(os.path.join(path, 'requirements.txt')),
    "Node": lambda path: os.path.exists(os.path.join(path, 'package.json')),
    "Java": lambda path: os.path.exists(os.path.join(path, 'pom.xml')) or \
                         os.path.exists(os.path.join(path, 'build.gradle')),
    "Go": lambda path: os.path.exists(os.path.join(path, 'go.mod')),
    "Rust": lambda path: os.path.exists(os.path.join(path, 'Cargo.toml')),
    "Ruby": lambda path: os.path.exists(os.path.join(path, 'Gemfile')),
    "Flutter": lambda path: os.path.exists(os.path.join(path, 'pubspec.yaml')),

    # Game Engines
    "Unity": lambda path: os.path.isdir(os.path.join(path, 'Assets')) and \
                          os.path.isdir(os.path.join(path, 'ProjectSettings')),

    # IDEs & Editors
    "VisualStudioCode": lambda path: os.path.isdir(os.path.join(path, '.vscode')),
    "VisualStudio": lambda path: any(f.endswith(('.sln', '.csproj')) for f in os.listdir(path)),
    "JetBrains": lambda path: os.path.isdir(os.path.join(path, '.idea')),
}

def detect_technologies(project_path: str) -> List[str]:
    """
    Analyzes a directory to detect the technologies and tools used.

    It iterates through a set of predefined rules to identify technologies
    based on the presence of specific files or folders. It also automatically
    adds the host operating system to the list.

    Args:
        project_path: The absolute path to the user's project directory.

    Returns:
        A list of strings, where each string is a detected technology or OS.
        Returns an empty list if the path is invalid.
    """
    if not os.path.isdir(project_path):
        return []

    detected = []
    
    try:
        # Check technology rules
        for tech, rule in DETECTION_RULES.items():
            if rule(project_path):
                detected.append(tech)
    except OSError as e:
        # Handle cases where we don't have permission to list directories
        print(f"Could not analyze path {project_path}: {e}")
        return [f"Error accessing {os.path.basename(project_path)}"]

    # Always add OS-specific rules
    os_name = platform.system()
    if os_name == 'Windows':
        detected.append('Windows')
    elif os_name == 'Darwin': # Darwin is the core of macOS
        detected.append('macOS')
    
    # Using set to remove potential duplicates before returning as list
    return sorted(list(set(detected)))