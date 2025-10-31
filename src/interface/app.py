# src/interface/app.py

import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
import pyperclip
import os

# Importar las funciones de las otras capas
from src.infrastructure.file_analyzer import detect_technologies
from src.infrastructure.template_loader import get_template_content
from src.core.use_cases import generate_gitignore_content

class App(ctk.CTk, TkinterDnD.DnDWrapper):
    """
    The main application class for GitIgnore Genius.

    This class builds the graphical user interface using CustomTkinter and
    handles the drag-and-drop functionality using TkinterDnD2.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

        # --- MEJORA 3: Estética y MEJORA 4: Icono ---
        self.title("🐍 GitIgnore Genius")
        self.geometry("600x700")
        ctk.set_appearance_mode("dark")
        self.minsize(500, 600)

        # Cargar el icono de la ventana (debe estar en la raíz del proyecto)
        icon_path = "icon.ico"
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        # --- MEJORA 1: Colores para Feedback Visual ---
        self.DROP_BG_COLOR = ctk.ThemeManager.theme["CTkFrame"]["fg_color"]
        self.DROP_HOVER_COLOR = "#1F6AA5" # Un azul distintivo para el hover

        # --- Widget Creation ---
        self.create_widgets()

    def create_widgets(self):
        """Creates and configures all the UI widgets for the application."""
        # MEJORA 3: Añadimos más padding para que "respire" la interfaz
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(padx=25, pady=25, fill="both", expand=True)

        # 1. Drop Zone (Label)
        self.drop_label = ctk.CTkLabel(
            self.main_frame,
            text="📂\n\nDrag & Drop Your Project Folder Here",
            font=ctk.CTkFont(size=20, weight="bold"),
            fg_color=self.DROP_BG_COLOR,
            corner_radius=10,
            text_color=("gray20", "gray80")
        )
        self.drop_label.pack(fill="x", pady=(0, 20), ipady=40)

        # 2. Result Textbox
        self.result_textbox = ctk.CTkTextbox(
            self.main_frame,
            font=ctk.CTkFont(family="monospace", size=13),
            state="disabled",
            corner_radius=10,
            border_width=2 # MEJORA 3: Un borde para mejor definición
        )
        self.result_textbox.pack(fill="both", expand=True, pady=(0, 20))

        # 3. Copy Button
        self.copy_button = ctk.CTkButton(
            self.main_frame,
            text="Copy to Clipboard",
            font=ctk.CTkFont(size=14, weight="bold"),
            state="disabled",
            command=self.copy_to_clipboard,
        )
        self.copy_button.pack(fill="x", ipady=8)

        # --- Drag & Drop Setup ---
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.handle_drop)

        # --- MEJORA 1: Bindeo de eventos para Feedback Visual ---
        self.drop_label.bind("<Enter>", self.on_enter_drop_zone)
        self.drop_label.bind("<Leave>", self.on_leave_drop_zone)

    # --- MEJORA 1: Funciones para manejar el hover en la Drop Zone ---
    def on_enter_drop_zone(self, event):
        """Changes the drop zone color when the mouse enters."""
        self.drop_label.configure(fg_color=self.DROP_HOVER_COLOR)

    def on_leave_drop_zone(self, event):
        """Resets the drop zone color when the mouse leaves."""
        self.drop_label.configure(fg_color=self.DROP_BG_COLOR)

    def handle_drop(self, event):
        """
        Handles the event when a folder is dropped onto the window.
        This method orchestrates the entire application logic flow.
        """
        project_path = event.data.strip('{}')
        self.update_ui_for_processing()
        detected = detect_technologies(project_path)
        gitignore_text = generate_gitignore_content(detected, get_template_content)
        self.update_ui_with_result(gitignore_text)
        self.on_leave_drop_zone(None) # Resetea el color después de un drop

    def update_ui_for_processing(self):
        """Provides visual feedback that processing has started."""
        self.result_textbox.configure(state="normal")
        self.result_textbox.delete("1.0", "end")
        self.result_textbox.insert("1.0", "🧠 Analyzing project...")
        self.result_textbox.configure(state="disabled")
        self.copy_button.configure(state="disabled")
        self.update_idletasks()

    def update_ui_with_result(self, text: str):
        """Displays the generated .gitignore content in the UI."""
        self.result_textbox.configure(state="normal")
        self.result_textbox.delete("1.0", "end")
        self.result_textbox.insert("1.0", text)
        self.result_textbox.configure(state="disabled")
        self.copy_button.configure(state="normal", fg_color=self.DROP_HOVER_COLOR, text="Copy to Clipboard")

    def copy_to_clipboard(self):
        """Copies the content of the result textbox to the system clipboard."""
        content = self.result_textbox.get("1.0", "end-1c")
        pyperclip.copy(content)
        self.copy_button.configure(text="✅ Copied!", fg_color="#107C41")
        self.after(2000, lambda: self.copy_button.configure(text="Copy to Clipboard", fg_color=self.DROP_HOVER_COLOR))