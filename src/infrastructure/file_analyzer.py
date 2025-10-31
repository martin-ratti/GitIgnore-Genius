# src/infrastructure/file_analyzer.py

import os
import platform
from typing import List, Dict, Callable

# Define a type for our detection rules for clarity
DetectionRule = Callable[[str], bool]

# Define the "fingerprints" for each technology.
DETECTION_RULES: Dict[str, DetectionRule] = {
    # Languages & Frameworks
    "Python": lambda path: any(f.endswith('.py') for f in os.listdir(path)) or \
                           os.path.exists(os.path.join(path, 'requirements.txt')),
    "Node": lambda path: os.path.exists(os.path.join(path, 'package.json')),
    "Java": lambda path: os.path.exists(os.path.join(path, 'pom.xml')) or \
                         ("build.gradle" in os.listdir(path) and any(f.endswith(".java") for f in os.listdir(path))),
    "Kotlin": lambda path: any(f.endswith(('.kt', '.kts')) for f in os.listdir(path)),
    "Go": lambda path: os.path.exists(os.path.join(path, 'go.mod')),
    "Rust": lambda path: os.path.exists(os.path.join(path, 'Cargo.toml')),
    "Ruby": lambda path: os.path.exists(os.path.join(path, 'Gemfile')),
    "PHP": lambda path: os.path.exists(os.path.join(path, 'composer.json')) or \
                        any(f.endswith('.php') for f in os.listdir(path)),
    "Swift": lambda path: any(f.endswith('.swift') for f in os.listdir(path)),
    "C++": lambda path: any(f.endswith(('.cpp', '.c', '.h', '.hpp')) for f in os.listdir(path)) or \
                        os.path.exists(os.path.join(path, 'CMakeLists.txt')),
    "Flutter": lambda path: os.path.exists(os.path.join(path, 'pubspec.yaml')),

    # Game Engines
    "Unity": lambda path: os.path.isdir(os.path.join(path, 'Assets')) and \
                          os.path.isdir(os.path.join(path, 'ProjectSettings')),

    # IDEs & Platforms
    "VisualStudio": lambda path: any(f.endswith(('.sln', '.csproj', '.fsproj', '.vbproj')) for f in os.listdir(path)),
    "VisualStudioCode": lambda path: os.path.isdir(os.path.join(path, '.vscode')),
    "JetBrains": lambda path: os.path.isdir(os.path.join(path, '.idea')),
    "Xcode": lambda path: os.path.isdir(os.path.join(path, '.xcodeproj')) or \
                       os.path.isdir(os.path.join(path, '.xcworkspace')),
    "AndroidStudio": lambda path: os.path.exists(os.path.join(path, 'build.gradle')) and \
                               os.path.exists(os.path.join(path, 'app/src.main/AndroidManifest.xml')),
}

def detect_technologies(project_path: str) -> List[str]:
    """
    Analyzes a directory to detect the technologies and tools used.
    """
    if not os.path.isdir(project_path):
        return []

    detected = []
    
    try:
        for tech, rule in DETECTION_RULES.items():
            if rule(project_path):
                detected.append(tech)
    except (OSError, FileNotFoundError) as e:
        print(f"Could not fully analyze path {project_path}: {e}")
        # Continue with what has been detected so far

    # Always add OS-specific rules
    os_name = platform.system()
    if os_name == 'Windows':
        detected.append('Windows')
    elif os_name == 'Darwin': # Darwin is the core of macOS
        detected.append('macOS')
    
    return sorted(list(set(detected)))