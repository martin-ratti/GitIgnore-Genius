import customtkinter as ctk
from tkinter import filedialog, StringVar
from tkinterdnd2 import DND_FILES, TkinterDnD
import pyperclip
import os
import platform
from typing import Dict, List

from src.infrastructure.file_analyzer import CATEGORIZED_DETECTION_RULES, detect_technologies
from src.infrastructure.template_loader import get_template_content
from src.core.use_cases import generate_gitignore_content

class App(ctk.CTk, TkinterDnD.DnDWrapper):
    """Main application class for GitIgnore Genius."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

        self.title("🐍 GitIgnore Genius")
        self.geometry("800x700")
        ctk.set_appearance_mode("dark")
        self.minsize(700, 600)

        icon_path = "icon.ico"
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        self.current_project_path = None
        self.checkbox_vars: Dict[str, StringVar] = {}

        # [FIX] Definición de colores (se eliminan las variables de borde no usadas)
        self.DROP_DEFAULT_BG_COLOR = ctk.ThemeManager.theme["CTkFrame"]["fg_color"]
        self.DROP_HOVER_BG_COLOR = "#1F6AA5" # Azul oscuro para el fondo

        self.DROP_TEXT_DEFAULT = "📂\n\nArrastra la carpeta de tu proyecto aquí\n(o haz clic para buscar)"
        self.DROP_TEXT_HOVER = "⏬\n\n¡Suelta la carpeta o haz clic para buscar!"

        self.create_widgets()

    def create_widgets(self):
        """Creates and configures all the UI widgets."""
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(padx=25, pady=25, fill="both", expand=True)

        self.drop_label = ctk.CTkLabel(
            self.main_frame, text=self.DROP_TEXT_DEFAULT,
            font=ctk.CTkFont(size=20, weight="bold"),
            fg_color=self.DROP_DEFAULT_BG_COLOR,
            # [FIX] Se eliminan 'border_color' y 'border_width' (no soportados)
            corner_radius=10,
            text_color=("gray20", "gray80"),
            cursor="hand2" # [REFAC] Cursor de mano para indicar que es clicable
        )
        self.drop_label.pack(fill="x", pady=(0, 20), ipady=20)

        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=2)
        self.content_frame.grid_rowconfigure(0, weight=1)

        self.checklist_frame = ctk.CTkScrollableFrame(
            self.content_frame, label_text="Plantillas Disponibles"
        )
        self.checklist_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 20))
        self.populate_checklist(detected_by_category={})
        
        self.result_textbox = ctk.CTkTextbox(
            self.content_frame, font=ctk.CTkFont(family="monospace", size=13),
            corner_radius=10, border_width=2,
            state="normal"
        )
        self.result_textbox.grid(row=0, column=1, sticky="nsew")

        self.status_label = ctk.CTkLabel(
            self.main_frame, text="", text_color="#E63946",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.status_label.pack(fill="x", pady=(10, 10))

        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.pack(fill="x")
        self.button_frame.grid_columnconfigure((0, 1), weight=1)

        self.copy_button = ctk.CTkButton(
            self.button_frame, text="Copy to Clipboard",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.copy_to_clipboard
        )
        self.copy_button.grid(row=0, column=0, padx=(0, 10), sticky="ew")

        self.save_button = ctk.CTkButton(
            self.button_frame, text="Save to File...",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.save_to_file
        )
        self.save_button.grid(row=0, column=1, padx=(10, 0), sticky="ew")

        # --- Bindings ---
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.handle_drop)
        
        # [REFAC] Bindings para hover y clic en el drop_label
        self.drop_label.bind("<Enter>", self.on_enter_drop_zone)
        self.drop_label.bind("<Leave>", self.on_leave_drop_zone)
        self.drop_label.bind("<Button-1>", self.handle_click_browse)

        self.show_welcome_message()

    def populate_checklist(self, detected_by_category: Dict[str, List[str]]):
        """(Re)Crea los checkboxes de plantillas, agrupados por categoría."""
        for widget in self.checklist_frame.winfo_children():
            widget.destroy()
        self.checkbox_vars.clear()

        all_rules = CATEGORIZED_DETECTION_RULES.copy()

        for category, rules in all_rules.items():
            category_label = ctk.CTkLabel(
                self.checklist_frame, text=category,
                font=ctk.CTkFont(size=14, weight="bold")
            )
            category_label.pack(fill="x", pady=(10, 5))

            for tech_name in rules.keys():
                var = ctk.StringVar(value="off")
                if tech_name in detected_by_category.get(category, []):
                    var.set("on")
                
                checkbox = ctk.CTkCheckBox(
                    self.checklist_frame, text=tech_name, variable=var,
                    onvalue="on", offvalue="off",
                    command=self.regenerate_content
                )
                checkbox.pack(fill="x", padx=20)
                self.checkbox_vars[tech_name] = var

    def regenerate_content(self):
        """
        Lee todos los checkboxes, genera el .gitignore y actualiza el textbox.
        """
        self.status_label.configure(text="")
        
        selected_techs = [
            tech for tech, var in self.checkbox_vars.items() if var.get() == "on"
        ]
        
        try:
            gitignore_text = generate_gitignore_content(
                selected_techs, get_template_content
            )
            self.update_ui_with_result(gitignore_text)
        except FileNotFoundError as e:
            error_msg = f"Error: {e}. Desmarca la plantilla."
            self.status_label.configure(text=error_msg)
        except Exception as e:
            self.status_label.configure(text=f"Error inesperado: {str(e)}")

    def show_welcome_message(self):
        """Muestra el mensaje de bienvenida en el textbox editable."""
        self.result_textbox.delete("1.0", "end")
        welcome_text = (
            "¡Bienvenido a GitIgnore Genius! 🚀\n\n"
            "1. Arrastra la carpeta de tu proyecto al área de arriba.\n"
            "2. O haz clic en el área para buscar la carpeta.\n"
            "3. Las plantillas detectadas se marcarán a la izquierda.\n"
            "4. Añade o quita las que necesites.\n"
            "5. Edita, copia o guarda tu .gitignore final."
        )
        self.result_textbox.insert("1.0", welcome_text)

    # [FIX] Se elimina 'border_color' y 'border_width' (no soportados)
    def on_enter_drop_zone(self, event):
        """Cambia el texto y color del drop_label al entrar."""
        self.drop_label.configure(
            text=self.DROP_TEXT_HOVER,
            fg_color=self.DROP_HOVER_BG_COLOR
        )

    # [FIX] Se elimina 'border_color' y 'border_width' (no soportados)
    def on_leave_drop_zone(self, event):
        """Restaura el texto y color del drop_label al salir."""
        self.drop_label.configure(
            text=self.DROP_TEXT_DEFAULT,
            fg_color=self.DROP_DEFAULT_BG_COLOR
        )

    # [REFAC] Nueva función para manejar el clic
    def handle_click_browse(self, event=None):
        """Abre el diálogo 'askdirectory' y procesa la carpeta."""
        project_path = filedialog.askdirectory(
            initialdir=self.current_project_path or os.path.expanduser("~"),
            title="Selecciona la carpeta de tu proyecto"
        )
        if project_path and os.path.isdir(project_path):
            self.process_project_path(project_path)

    def handle_drop(self, event):
        """Maneja el drop, extrae el path y lo procesa."""
        project_path = event.data.strip('{}')
        if project_path and os.path.isdir(project_path):
            self.process_project_path(project_path)
        else:
            self.show_error_message(f"Error: La ruta soltada no es un directorio válido.")
            self.on_leave_drop_zone(None)

    # [REFAC] Lógica de análisis extraída a su propia función
    def process_project_path(self, project_path: str):
        """
        Función central para analizar un project_path (desde drop o clic)
        y actualizar la UI.
        """
        self.current_project_path = project_path
        self.status_label.configure(text="")
        
        self.drop_label.configure(text=f"Analizando: {os.path.basename(project_path)}...")
        self.update_idletasks() # Forzar actualización de UI
        
        try:
            all_detected, detected_by_category = detect_technologies(project_path)
            
            self.populate_checklist(detected_by_category)
            self.regenerate_content()
            
            if all_detected:
                self.drop_label.configure(text=f"¡Listo! Detectadas: {', '.join(all_detected)}")
            else:
                 self.drop_label.configure(text="No se detectó tecnología (puedes elegir manualmente)")
            
        except Exception as e:
            self.show_error_message(f"Error inesperado al analizar: {str(e)}")
        
        # Restaura el estado visual de la drop_label (color y texto)
        self.after(2500, lambda: self.on_leave_drop_zone(None))

    def show_error_message(self, message: str):
        """Miyestra un error y resetea la UI."""
        self.status_label.configure(text=message)
        self.show_welcome_message()
        self.drop_label.configure(text=self.DROP_TEXT_DEFAULT)
        self.populate_checklist(detected_by_category={})

    def update_ui_with_result(self, text: str):
        """Muestra el contenido generado en el textbox."""
        self.result_textbox.delete("1.0", "end")
        self.result_textbox.insert("1.0", text)

    def copy_to_clipboard(self):
        """Copia el contenido del textbox (que puede estar editado)."""
        content = self.result_textbox.get("1.0", "end-1c")
        pyperclip.copy(content)
        self.copy_button.configure(text="✅ Copied!", fg_color="#107C41")
        self.save_button.configure(text="Save to File...", fg_color=self.DROP_HOVER_BG_COLOR)
        self.after(2000, lambda: self.copy_button.configure(text="Copy to Clipboard", fg_color=self.DROP_HOVER_BG_COLOR))

    def save_to_file(self):
        """Guarda el contenido del textbox (que puede estar editado)."""
        content = self.result_textbox.get("1.0", "end-1c")
        
        file_path = filedialog.asksaveasfilename(
            initialdir=self.current_project_path or os.path.expanduser("~"),
            initialfile=".gitignore",
            defaultextension=".gitignore",
            filetypes=[("Git Ignore File", ".gitignore"), ("All Files", "*.*")]
        )
        
        if file_path:
            try:
                # [FIX] Corregido el error tipográfico file_ápath -> file_path
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.save_button.configure(text="✅ Saved!", fg_color="#107C41")
                self.copy_button.configure(text="Copy to Clipboard", fg_color=self.DROP_HOVER_BG_COLOR)
                self.after(2000, lambda: self.save_button.configure(text="Save to File...", fg_color=self.DROP_HOVER_BG_COLOR))
            
            except OSError as e:
                self.show_error_message(f"Error al guardar: {e}")

