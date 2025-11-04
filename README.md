````markdown
# 📜 GitIgnore Genius

**Una aplicación de escritorio simple e inteligente para generar archivos `.gitignore` personalizados para tus proyectos.**

!

---

## ✨ Características

* **🔍 Detección Automática:** Arrastra un proyecto y la app sugerirá plantillas basadas en los lenguajes, frameworks e IDEs que encuentre.
* **🎛️ Control Total:** Selecciona, deselecciona y edita manualmente las plantillas para crear el `.gitignore` perfecto para tus necesidades.
* **📚 Amplia Biblioteca:** Incluye docenas de plantillas robustas y seguras basadas en los estándares de la comunidad.
* **💾 Guardado Directo:** Guarda el resultado directamente como un archivo `.gitignore` en tu proyecto con un solo clic.
* **📦 Ejecutable Simple:** Empaquetado como un único archivo `.exe` para Windows que no requiere instalación.

---

## 🚀 Cómo Usar

1.  Descarga la última versión del `.exe` desde la sección de **[Releases](https://github.com/TU_USUARIO/GitIgnore-Genius/releases)** de este repositorio.
2.  Ejecuta `GitIgnoreGenius.exe`.
3.  Arrastra la carpeta de tu proyecto sobre la ventana. Las tecnologías detectadas se marcarán automáticamente en la lista de la izquierda.
4.  **Añade o quita** las plantillas que necesites usando los checkboxes. El resultado se actualizará en tiempo real.
5.  **Edita** el texto directamente en el panel de la derecha si necesitas añadir reglas personalizadas.
6.  Haz clic en **"Copy to Clipboard"** para copiar el resultado o en **"Save to File..."** para guardarlo directamente en tu proyecto.

---

## ⚠️ ¡Importante! Revisa Siempre el Resultado

Aunque las plantillas están basadas en las mejores prácticas, cada proyecto es único. Antes de confirmar tu `.gitignore`, **tómate un momento para revisarlo** y asegurarte de que no esté ignorando accidentalmente archivos que necesites versionar (como scripts de migración o configuraciones específicas).

> 💡 Recuerda: Tú eres el responsable final del contenido de tu repositorio.

---

## 🛠️ Para Desarrolladores (Compilar desde la Fuente)

Si deseas modificar o compilar el proyecto tú mismo, sigue estos pasos:

### 1. Clona el repositorio

```bash
git clone [https://github.com/TU_USUARIO/GitIgnore-Genius.git](https://github.com/TU_USUARIO/GitIgnore-Genius.git)
cd GitIgnore-Genius
````

### 2\. Crea y activa un entorno virtual

```bash
python -m venv venv
.\venv\Scripts\Activate
```

### 3\. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4\. Ejecuta la aplicación

```bash
python main.py
```

### 5\. Compila el ejecutable (One-File)

```bash
pyinstaller --noconsole --name GitIgnoreGenius --icon="icon.ico" --add-data "src/infrastructure/templates;templates" main.py
```

-----

## 🤝 Cómo Contribuir (Añadir Plantillas)

¡Las contribuciones son bienvenidas\! Si quieres añadir soporte para una nueva tecnología, el proceso es muy sencillo:

1.  **Fork y Clona:** Haz un "Fork" del repositorio y clónalo en tu máquina.
2.  **Crea la Plantilla:** Añade un nuevo archivo `.gitignore` a la carpeta `src/infrastructure/templates/`. El nombre del archivo debe ser el nombre de la tecnología (ej. `Terraform.gitignore`).
3.  **Añade la Regla de Detección:**
      * Abre el archivo `src/infrastructure/file_analyzer.py`.
      * Busca el diccionario `CATEGORIZED_DETECTION_RULES`.
      * Añade una nueva entrada en la categoría correspondiente. La clave debe ser **exactamente el mismo nombre** que le diste a tu archivo de plantilla (sin la extensión). El valor debe ser una función `lambda` que detecte una "huella digital" de esa tecnología.
      * **Ejemplo para Terraform:**
        ```python
        # Dentro de una categoría, por ejemplo "Infraestructura":
        "Terraform": lambda path: any(f.endswith('.tf') for f in os.listdir(path)),
        ```
4.  **Crea un Pull Request:** Envía un Pull Request con tus cambios para que puedan ser revisados e integrados.

-----

## 🧩 Tecnologías Utilizadas

  * Python 🐍
  * CustomTkinter & TkinterDnD2
  * PyInstaller 📦
  * Plantillas `.gitignore` oficiales de la comunidad de GitHub.

-----

## 📜 Licencia

Este proyecto puedes usarlo, modificarlo y distribuirlo libremente, siempre citando la autoría correspondiente.

-----

Hecho con ❤️ por **[Martín Ratti](https://www.google.com/search?q=https://github.com/martin-ratti)**

```
```
