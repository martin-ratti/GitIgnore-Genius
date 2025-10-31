# src/infrastructure/file_analyzer.py
import os
import platform
from typing import List, Dict, Callable

DetectionRule = Callable[[str], bool]

# Para añadir una nueva tecnología:
# 1. Añade su plantilla .gitignore en la carpeta 'templates'.
# 2. Añade una nueva entrada en este diccionario en la categoría correcta.
DETECTION_RULES: Dict[str, DetectionRule] = {
    # --- Lenguajes de Programación ---
    "Python": lambda path: any(f.endswith('.py') for f in os.listdir(path)) or \
                           os.path.exists(os.path.join(path, 'requirements.txt')),
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
    
    # --- Frameworks (Web y Fullstack) ---
    "Node": lambda path: os.path.exists(os.path.join(path, 'package.json')),
    "Angular": lambda path: os.path.exists(os.path.join(path, 'angular.json')),
    "React": lambda path: os.path.exists(os.path.join(path, 'public/index.html')) and \
                          os.path.exists(os.path.join(path, 'src/index.js')),
    "Vue": lambda path: os.path.exists(os.path.join(path, 'vue.config.js')) or \
                       os.path.exists(os.path.join(path, 'src/main.js')),
    "Svelte": lambda path: os.path.exists(os.path.join(path, 'svelte.config.js')),
    "NextJS": lambda path: os.path.exists(os.path.join(path, 'next.config.js')),
    "Astro": lambda path: any(f.startswith('astro.config.') for f in os.listdir(path)),
    "Django": lambda path: os.path.exists(os.path.join(path, 'manage.py')),
    "Laravel": lambda path: os.path.exists(os.path.join(path, 'artisan')),

    # --- Frameworks (Móvil) ---
    "Flutter": lambda path: os.path.exists(os.path.join(path, 'pubspec.yaml')),
    "ReactNative": lambda path: os.path.exists(os.path.join(path, 'app.json')),

    # --- ORMs y Bases de Datos ---
    "Prisma": lambda path: os.path.isdir(os.path.join(path, 'prisma')),
    "SQLite": lambda path: any(f.endswith(('.db', '.sqlite', '.sqlite3')) for f in os.listdir(path)),
    "MySQL": lambda path: os.path.exists(os.path.join(path, 'my.cnf')) or any(f.endswith('.mysql') for f in os.listdir(path)),
    "PostgreSQL": lambda path: os.path.exists(os.path.join(path, 'postgresql.conf')) or any(f.endswith('.pgdump') for f in os.listdir(path)),
    "SQLServer": lambda path: any(f.endswith(('.mdf', '.ldf')) for f in os.listdir(path)),
    "MongoDB": lambda path: os.path.exists(os.path.join(path, 'mongod.conf')),
    "Redis": lambda path: os.path.exists(os.path.join(path, 'redis.conf')) or os.path.exists(os.path.join(path, 'dump.rdb')),
    
    # --- Motores de Videojuegos ---
    "Unity": lambda path: os.path.isdir(os.path.join(path, 'Assets')) and \
                          os.path.isdir(os.path.join(path, 'ProjectSettings')),

    # --- IDEs y Plataformas ---
    "VisualStudio": lambda path: any(f.endswith(('.sln', '.csproj', '.fsproj', '.vbproj')) for f in os.listdir(path)),
    "VisualStudioCode": lambda path: os.path.isdir(os.path.join(path, '.vscode')),
    "JetBrains": lambda path: os.path.isdir(os.path.join(path, '.idea')),
    "Xcode": lambda path: os.path.isdir(os.path.join(path, '.xcodeproj')) or \
                       os.path.isdir(os.path.join(path, '.xcworkspace')),
    "AndroidStudio": lambda path: os.path.exists(os.path.join(path, 'settings.gradle')),
}

def detect_technologies(project_path: str) -> List[str]:
    """Analyzes a directory to detect the technologies and tools used."""
    if not os.path.isdir(project_path):
        return []

    detected = []
    try:
        # List files once for efficiency, as some rules might re-use it
        files_in_project = os.listdir(project_path)
        for tech, rule in DETECTION_RULES.items():
            # The lambda will use its own logic, but having the list here is a good practice
            if rule(project_path):
                detected.append(tech)
    except (OSError, FileNotFoundError) as e:
        print(f"Could not fully analyze path {project_path}: {e}")

    os_name = platform.system()
    if os_name == 'Windows':
        detected.append('Windows')
    elif os_name == 'Darwin':
        detected.append('macOS')
    
    return sorted(list(set(detected)))