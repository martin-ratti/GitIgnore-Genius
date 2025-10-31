📜 GitIgnore Genius

Una aplicación de escritorio simple e inteligente para generar archivos .gitignore personalizados para tus proyectos!

✨ Características

Detección Automática: Arrastra y suelta la carpeta de tu proyecto y la app detectará automáticamente los lenguajes, frameworks e IDEs utilizados.

Plantillas Robustas: Utiliza plantillas de .gitignore estándar de la comunidad para asegurar una cobertura completa y segura.

Interfaz Simple: Una experiencia de usuario limpia y directa: arrastra, genera y copia.

Multiplataforma: Empaquetado como un ejecutable simple para Windows.

🚀 Cómo Usar

Descarga la última versión del .exe desde la sección de Releases de este repositorio.

Ejecuta GitIgnoreGenius.exe.

Arrastra la carpeta de tu proyecto sobre la ventana de la aplicación.

El contenido del .gitignore se generará instantáneamente.

Haz clic en "Copy to Clipboard" y pega el contenido en un archivo .gitignore en tu proyecto.

⚠️ ¡Importante! Revisa Siempre el Resultado

Aunque las plantillas están basadas en las mejores prácticas de la comunidad, cada proyecto es único. Antes de confirmar tu .gitignore, tómate un momento para revisarlo y asegurarte de que no esté ignorando accidentalmente un archivo que necesites versionar (como scripts de migración, archivos de configuración específicos o assets importantes).

Tú eres el responsable final del contenido de tu repositorio.

🛠️ Para Desarrolladores (Cómo Compilar desde la Fuente)

Si deseas modificar o compilar el proyecto tú mismo, sigue estos pasos:

Clona el repositorio:

git clone [https://github.com/TU_USUARIO/GitIgnore-Genius.git](https://github.com/TU_USUARIO/GitIgnore-Genius.git)
cd GitIgnore-Genius


Crea y activa un entorno virtual:

python -m venv venv
.\venv\Scripts\Activate


Instala las dependencias:

pip install -r requirements.txt


Ejecuta la aplicación:

python main.py


Para compilar el ejecutable:

pyinstaller --noconsole --name GitIgnoreGenius --icon="icon.ico" --add-data "src/infrastructure/templates;src/infrastructure/templates" main.py
