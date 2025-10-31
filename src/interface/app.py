# src/interface/app.py
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
import pyperclip
import os
from src.infrastructure.file_analyzer import detect_technologies
from src.infrastructure.template_loader import get_template_content
from src.core.use_cases import generate_gitignore_content

class App(ctk.CTk, TkinterDnD.DnDWrapper):
    """Main application class for GitIgnore Genius."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

        self.title("🐍 GitIgnore Genius")
        self.geometry("600x700")
        ctk.set_appearance_mode("dark")
        self.minsize(500, 600)

        icon_path = "icon.ico"
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        self.DROP_BG_COLOR = ctk.ThemeManager.theme["CTkFrame"]["fg_color"]
        self.DROP_HOVER_COLOR = "#1F6AA5"

        self.create_widgets()

    def create_widgets(self):
        """Creates and configures all the UI widgets."""
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(padx=25, pady=25, fill="both", expand=True)

        self.drop_label = ctk.CTkLabel(
            self.main_frame, text="📂\n\nDrag & Drop Your Project Folder Here",
            font=ctk.CTkFont(size=20, weight="bold"), fg_color=self.DROP_BG_COLOR,
            corner_radius=10, text_color=("gray20", "gray80")
        )
        self.drop_label.pack(fill="x", pady=(0, 20), ipady=40)

        self.result_textbox = ctk.CTkTextbox(
            self.main_frame, font=ctk.CTkFont(family="monospace", size=13),
            state="disabled", corner_radius=10, border_width=2
        )
        self.result_textbox.pack(fill="both", expand=True, pady=(0, 20))

        self.copy_button = ctk.CTkButton(
            self.main_frame, text="Copy to Clipboard",
            font=ctk.CTkFont(size=14, weight="bold"),
            state="disabled", command=self.copy_to_clipboard
        )
        self.copy_button.pack(fill="x", ipady=8)

        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.handle_drop)
        self.drop_label.bind("<Enter>", self.on_enter_drop_zone)
        self.drop_label.bind("<Leave>", self.on_leave_drop_zone)

    def on_enter_drop_zone(self, event):
        self.drop_label.configure(fg_color=self.DROP_HOVER_COLOR)

    def on_leave_drop_zone(self, event):
        self.drop_label.configure(fg_color=self.DROP_BG_COLOR)

    def handle_drop(self, event):
        project_path = event.data.strip('{}')
        self.update_ui_for_processing()
        detected = detect_technologies(project_path)
        gitignore_text = generate_gitignore_content(detected, get_template_content)
        self.update_ui_with_result(gitignore_text)
        self.on_leave_drop_zone(None)

    def update_ui_for_processing(self):
        self.result_textbox.configure(state="normal")
        self.result_textbox.delete("1.0", "end")
        self.result_textbox.insert("1.0", "🧠 Analyzing project...")
        self.result_textbox.configure(state="disabled")
        self.copy_button.configure(state="disabled")
        self.update_idletasks()

    def update_ui_with_result(self, text: str):
        self.result_textbox.configure(state="normal")
        self.result_textbox.delete("1.0", "end")
        self.result_textbox.insert("1.0", text)
        self.result_textbox.configure(state="disabled")
        self.copy_button.configure(state="normal", fg_color=self.DROP_HOVER_COLOR, text="Copy to Clipboard")

    def copy_to_clipboard(self):
        content = self.result_textbox.get("1.0", "end-1c")
        pyperclip.copy(content)
        self.copy_button.configure(text="✅ Copied!", fg_color="#107C41")
        self.after(2000, lambda: self.copy_button.configure(text="Copy to Clipboard", fg_color=self.DROP_HOVER_COLOR))