# 📜 GitIgnore Genius

Una aplicación de escritorio simple e inteligente para generar archivos `.gitignore` personalizados para tus proyectos.

!

## ✨ Características

* **Detección Automática:** Arrastra y suelta la carpeta de tu proyecto y la app detectará automáticamente los lenguajes, frameworks e IDEs utilizados.
* **Plantillas Robustas:** Utiliza plantillas de `.gitignore` estándar de la comunidad para asegurar una cobertura completa.
* **Interfaz Simple:** Una experiencia de usuario limpia y directa: arrastra, genera y copia.
* **Multiplataforma:** Empaquetado como un ejecutable simple para Windows.

## 🚀 Cómo Usar

1.  Descarga la última versión del `.exe` desde la sección de **Releases** de este repositorio.
2.  Ejecuta `GitIgnoreGenius.exe`.
3.  Arrastra la carpeta de tu proyecto sobre la ventana de la aplicación.
4.  El contenido del `.gitignore` se generará instantáneamente.
5.  Haz clic en **"Copy to Clipboard"** y pega el contenido en un archivo `.gitignore` en tu proyecto.

## 🛠️ Para Desarrolladores (Cómo Compilar desde la Fuente)

Si deseas modificar o compilar el proyecto tú mismo, sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/TuUsuario/GitIgnore-Genius.git](https://github.com/TuUsuario/GitIgnore-Genius.git)
    cd GitIgnore-Genius
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación:**
    ```bash
    python main.py
    ```

5.  **Para compilar el ejecutable:**
    ```bash
    pyinstaller --noconsole --name GitIgnoreGenius --icon="icon.ico" --add-data "src/infrastructure/templates;src/infrastructure/templates" main.py
    ```