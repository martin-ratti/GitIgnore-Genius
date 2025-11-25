<h1 align="center">📜 GitIgnore Genius</h1>

<div align="center">
    <img src="https://img.shields.io/badge/Estado-Estable-success?style=for-the-badge&logo=check&logoColor=white" alt="Estado Badge"/>
    <img src="https://img.shields.io/badge/Versión-1.0.0-blue?style=for-the-badge" alt="Version Badge"/>
</div>

<p align="center">
    <a href="https://github.com/martin-ratti" target="_blank" style="text-decoration: none;">
        <img src="https://img.shields.io/badge/👤%20Martín%20Ratti-martin--ratti-000000?style=for-the-badge&logo=github&logoColor=white" alt="Martin"/>
    </a>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
    <img src="https://img.shields.io/badge/GUI-CustomTkinter-2B2B2B?style=for-the-badge&logo=tkinter&logoColor=white" alt="CustomTkinter Badge"/>
    <img src="https://img.shields.io/badge/Drag%20%26%20Drop-TkinterDnD-orange?style=for-the-badge&logo=move&logoColor=white" alt="DnD Badge"/>
    <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Badge"/>
</p>

<hr>

<h2>🎯 Objetivo y Alcance</h2>

<p>
    <strong>GitIgnore Genius</strong> es una aplicación de escritorio inteligente diseñada para resolver el problema común de configurar archivos <code>.gitignore</code>.
    Su misión es analizar automáticamente la estructura de tu proyecto y generar un archivo de exclusión robusto y personalizado.
</p>

<p>
    Ya no es necesario copiar y pegar manualmente desde múltiples sitios. Simplemente arrastra tu carpeta y la aplicación detectará lenguajes, frameworks, 
    entornos y sistemas operativos, permitiéndote generar un archivo seguro con un solo clic.
</p>

<hr>

<h2>⚙️ Stack Tecnológico & Arquitectura</h2>

<p>El proyecto sigue los principios de <strong>Clean Architecture</strong> para asegurar mantenibilidad y fácil extensión de nuevas tecnologías.</p>

<table>
 <thead>
  <tr>
   <th>Capa / Componente</th>
   <th>Tecnología / Ruta</th>
   <th>Descripción</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td><strong>Interface (GUI)</strong></td>
   <td><code>src/interface/</code><br>(CustomTkinter)</td>
   <td>Maneja la interacción visual, el <em>Drag & Drop</em>, y el editor de texto integrado con resaltado de sintaxis básico.</td>
  </tr>
  <tr>
   <td><strong>Core (Dominio)</strong></td>
   <td><code>src/core/</code></td>
   <td>Lógica pura de negocio. Orquesta la combinación de múltiples plantillas en un único string coherente.</td>
  </tr>
  <tr>
   <td><strong>Infrastructure</strong></td>
   <td><code>src/infrastructure/</code><br>(File Analyzer)</td>
   <td>Implementa las reglas de detección (heurísticas) y carga las plantillas <code>.gitignore</code> desde el disco.</td>
  </tr>
  <tr>
   <td><strong>Empaquetado</strong></td>
   <td>PyInstaller</td>
   <td>Generación del ejecutable <em>single-file</em> con todos los recursos y plantillas embebidos.</td>
  </tr>
 </tbody>
</table>

<hr>

<h2>🚀 Características Principales</h2>

<ul>
    <li><strong>🔍 Detección Automática (Smart Scan)</strong>: Analiza "huellas digitales" en tu carpeta (ej. <code>package.json</code>, <code>venv/</code>, <code>.idea/</code>) para sugerir las plantillas correctas.</li>
    <li><strong>🎛️ Control Total</strong>: Panel lateral interactivo para activar o desactivar tecnologías detectadas manualmente.</li>
    <li><strong>📚 Amplia Biblioteca</strong>: Soporte nativo para decenas de tecnologías incluyendo Python, Node, React, Java, Unity, Flutter, macOS, Windows, y más.</li>
    <li><strong>✍️ Editor en Vivo</strong>: Puedes modificar el resultado generado directamente en la aplicación antes de guardarlo.</li>
    <li><strong>💾 Guardado Rápido</strong>: Funciones directas para copiar al portapapeles o guardar el archivo <code>.gitignore</code> en la raíz del proyecto.</li>
</ul>

<hr>

<h2>🛠️ Modo de Uso</h2>

<pre>
/GitIgnoreGenius
├── GitIgnoreGenius.exe    <-- La aplicación
└── icon.ico               <-- Icono del sistema
</pre>

<ol>
    <li><strong>Iniciar:</strong> Ejecuta <code>GitIgnoreGenius.exe</code>.</li>
    <li><strong>Analizar:</strong> Arrastra la carpeta de tu proyecto sobre la ventana o haz clic para buscarla.</li>
    <li><strong>Personalizar:</strong> Revisa las tecnologías marcadas en la lista izquierda. Añade o quita según necesites.</li>
    <li><strong>Editar (Opcional):</strong> Realiza ajustes manuales en el editor de texto de la derecha.</li>
    <li><strong>Exportar:</strong> Haz clic en <strong>"Save to File..."</strong> para guardar el archivo directamente en tu proyecto.</li>
</ol>

<hr>

<h2>🧑‍💻 Setup para Desarrolladores</h2>

Si deseas contribuir con nuevas plantillas o mejorar el código:

<h3>1. Configuración del Entorno</h3>
<pre><code># Clonar repositorio
git clone https://github.com/martin-ratti/GitIgnore-Genius.git

# Crear entorno virtual
python -m venv venv
.\venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt
</code></pre>

<h3>2. Ejecución en Desarrollo</h3>
<pre><code>python main.py</code></pre>

<h3>3. Compilación (.exe)</h3>
<p>Es necesario incluir la carpeta de plantillas en el ejecutable:</p>
<pre><code>pyinstaller --onefile --noconsole --name GitIgnoreGenius --icon="icon.ico" --add-data "src/infrastructure/templates;templates" main.py</code></pre>

<hr>

<h2>🤝 Cómo Contribuir (Añadir Plantillas)</h2>

Expandir la base de conocimientos es muy fácil:

1.  **Crear Plantilla:** Añade un archivo `.gitignore` en `src/infrastructure/templates/` (ej. `Terraform.gitignore`).
2.  **Definir Regla:** En `src/infrastructure/file_analyzer.py`, añade una entrada en `CATEGORIZED_DETECTION_RULES`:
    ```python
    "Terraform": lambda path: any(f.endswith('.tf') for f in os.listdir(path)),
    ```
3.  **Pull Request:** Envía tus cambios para revisión.

<hr>

<h2>⚖️ Créditos</h2>

<p>
    Desarrollado por <strong>Martín Ratti</strong>. Las plantillas base provienen de la colección oficial de GitHub y Toptal.
</p>
