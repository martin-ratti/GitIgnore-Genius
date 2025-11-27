<div align="center">

# 📜 GitIgnore Genius

<img src="https://img.shields.io/badge/Estado-Estable-success?style=for-the-badge&logo=check&logoColor=white" alt="Estado Badge"/>
<img src="https://img.shields.io/badge/Versión-1.0.0-blue?style=for-the-badge" alt="Version Badge"/>
<img src="https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge" alt="License Badge"/>

<br/>

<a href="https://github.com/martin-ratti" target="_blank" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/👤%20Martín%20Ratti-martin--ratti-000000?style=for-the-badge&logo=github&logoColor=white" alt="Martin"/>
</a>

<br/>

<p>
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
    <img src="https://img.shields.io/badge/Arquitectura-Clean%20Arch-orange?style=for-the-badge&logo=expertsexchange&logoColor=white" alt="Clean Arch Badge"/>
    <img src="https://img.shields.io/badge/GUI-CustomTkinter-2B2B2B?style=for-the-badge&logo=tkinter&logoColor=white" alt="CustomTkinter Badge"/>
    <img src="https://img.shields.io/badge/Drag%20%26%20Drop-TkinterDnD-orange?style=for-the-badge&logo=move&logoColor=white" alt="DnD Badge"/>
    <img src="https://img.shields.io/badge/Build-PyInstaller-0054a6?style=for-the-badge&logo=pypi&logoColor=white" alt="PyInstaller Badge"/>
    <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Badge"/>
</p>

</div>

---

## 🎯 Objetivo y Alcance

**GitIgnore Genius** es una aplicación de escritorio inteligente diseñada para resolver el problema común de configurar archivos `.gitignore`. Su misión es analizar automáticamente la estructura de tu proyecto y generar un archivo de exclusión robusto y personalizado.

Ya no es necesario copiar y pegar manualmente desde múltiples sitios. Simplemente arrastra tu carpeta y la aplicación detectará lenguajes, frameworks, entornos y sistemas operativos mediante **heurística avanzada**, permitiéndote generar un archivo seguro con un solo clic.

---

## 🏛️ Arquitectura y Diseño

El proyecto sigue los principios de **Clean Architecture** para asegurar mantenibilidad y fácil extensión de nuevas tecnologías.

### Diagrama de Componentes

| Capa | Componente | Descripción |
| :--- | :--- | :--- |
| **Interface** | `src/interface/` | Maneja la interacción visual con **CustomTkinter**, el *Drag & Drop*, y el editor de texto integrado. |
| **Core** | `src/core/` | Lógica pura de negocio. Orquesta la combinación de múltiples plantillas en un único string coherente. |
| **Infrastructure** | `src/infrastructure/` | Contiene el `File Analyzer` (reglas de detección) y el repositorio de plantillas `.gitignore`. |

-----

## 🚀 Características Principales

  * **🔍 Smart Scan (Heurística):** Analiza "huellas digitales" en tu carpeta (ej. `package.json`, `venv/`, `.idea/`, `Cargo.toml`) para sugerir las plantillas correctas automáticamente.
  * **🎛️ Control Total:** Panel lateral interactivo para activar o desactivar tecnologías detectadas manualmente.
  * **📚 Amplia Biblioteca:** Soporte nativo para decenas de tecnologías incluyendo:
      * **Lenguajes:** Python, Java, Node, Rust, Go, PHP, Swift, C++.
      * **Frameworks:** React, Angular, Vue, Flutter, Django, Laravel, NextJS.
      * **Herramientas:** Unity, VS Code, JetBrains, Windows, macOS, Linux.
  * **✍️ Editor en Vivo:** Puedes modificar el resultado generado directamente en la aplicación antes de guardarlo.
  * **💾 Exportación Flexible:** Funciones directas para copiar al portapapeles o guardar el archivo `.gitignore` en la raíz del proyecto.

-----

## 🛠️ Modo de Uso

```text
/GitIgnoreGenius
├── GitIgnoreGenius.exe    <-- La aplicación compilada
└── icon.ico               <-- Icono del sistema
```

1.  **Iniciar:** Ejecuta `GitIgnoreGenius.exe`.
2.  **Analizar:** Arrastra la carpeta de tu proyecto sobre la ventana o haz clic para buscarla.
3.  **Personalizar:** Revisa las tecnologías marcadas en la lista izquierda (detectadas automáticamente). Añade o quita según necesites.
4.  **Editar (Opcional):** Realiza ajustes manuales en el editor de texto de la derecha.
5.  **Exportar:** Haz clic en **"Save to File..."** para guardar el archivo directamente en tu proyecto.

-----

## 🧑‍💻 Setup para Desarrolladores

Si deseas contribuir con nuevas plantillas o mejorar el código:

### 1\. Configuración del Entorno

```bash
# Clonar repositorio
git clone [https://github.com/martin-ratti/GitIgnore-Genius.git](https://github.com/martin-ratti/GitIgnore-Genius.git)

# Crear entorno virtual
python -m venv venv
.\venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### 2\. Ejecución en Desarrollo

```bash
python main.py
```

### 3\. Compilación (.exe)

Es necesario incluir la carpeta de plantillas en el ejecutable para que funcione en modo "frozen":

```bash
pyinstaller --onefile --noconsole --name GitIgnoreGenius --icon="icon.ico" --add-data "src/infrastructure/templates;templates" main.py
```

-----

## 🤝 Cómo Contribuir (Añadir Plantillas)

Expandir la base de conocimientos es muy fácil gracias a la arquitectura modular:

1.  **Crear Plantilla:** Añade un archivo `.gitignore` en `src/infrastructure/templates/` (ej. `Terraform.gitignore`).

2.  **Definir Regla:** En `src/infrastructure/file_analyzer.py`, añade una entrada en `CATEGORIZED_DETECTION_RULES`. Puedes usar lambdas para detectar extensiones o archivos específicos:

    ```python
    "Terraform": lambda path: any(f.endswith('.tf') for f in os.listdir(path)),
    ```

3.  **Pull Request:** Envía tus cambios para revisión.

-----

## ⚖️ Créditos

Desarrollado por **Martín Ratti**.

  * Las plantillas base provienen de la colección oficial de [GitHub gitignore](https://github.com/github/gitignore) y [Toptal](https://www.toptal.com/developers/gitignore).
