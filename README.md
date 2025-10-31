````markdown
# 📜 GitIgnore Genius

**Una aplicación de escritorio simple e inteligente para generar archivos `.gitignore` personalizados para tus proyectos.**

---

## ✨ Características

- 🔍 **Detección Automática:**  
  Arrastra y suelta la carpeta de tu proyecto y la app detectará automáticamente los lenguajes, frameworks e IDEs utilizados.

- 📋 **Plantillas Robustas:**  
  Utiliza plantillas de `.gitignore` estándar de la comunidad para asegurar una cobertura completa y segura.

- 🖱️ **Interfaz Simple:**  
  Una experiencia de usuario limpia y directa: arrastra, genera y copia.

- 💻 **Multiplataforma:**  
  Empaquetado como un ejecutable simple para **Windows**.

---

## 🚀 Cómo Usar

1. Descarga la última versión del `.exe` desde la sección de **[Releases](../../releases)** de este repositorio.  
2. Ejecuta `GitIgnoreGenius.exe`.  
3. Arrastra la carpeta de tu proyecto sobre la ventana de la aplicación.  
4. El contenido del `.gitignore` se generará instantáneamente.  
5. Haz clic en **“Copy to Clipboard”** y pega el contenido en un archivo `.gitignore` dentro de tu proyecto.

---

## ⚠️ ¡Importante! Revisa Siempre el Resultado

Aunque las plantillas están basadas en las mejores prácticas de la comunidad, **cada proyecto es único**.  
Antes de confirmar tu `.gitignore`, tómate un momento para revisarlo y asegurarte de que no esté ignorando accidentalmente archivos que necesites versionar (como scripts de migración, configuraciones específicas o assets importantes).

> 💡 **Recuerda:** Tú eres el responsable final del contenido de tu repositorio.

---

## 🛠️ Para Desarrolladores (Compilar desde la Fuente)

Si deseas modificar o compilar el proyecto tú mismo, sigue estos pasos:

### 1️⃣ Clona el repositorio
```bash
git clone https://github.com/TU_USUARIO/GitIgnore-Genius.git
cd GitIgnore-Genius
````

### 2️⃣ Crea y activa un entorno virtual

```bash
python -m venv venv
.\venv\Scripts\Activate
```

### 3️⃣ Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecuta la aplicación

```bash
python main.py
```

### 5️⃣ Compila el ejecutable

```bash
pyinstaller --noconsole --name GitIgnoreGenius --icon="icon.ico" --add-data "src/infrastructure/templates;src/infrastructure/templates" main.py
```

---

## 🧩 Tecnologías Utilizadas

* Python 🐍
* PyInstaller 📦
* Tkinter
* Plantillas oficiales de GitHub `.gitignore`

---

## 📜 Licencia

Este proyecto puedes usarlo, modificarlo y distribuirlo libremente, siempre citando la autoría correspondiente.

---

### 💡 Hecho con ❤️ por [Martín Ratti](https://github.com/martin-ratti)

```
```
