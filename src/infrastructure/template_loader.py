# src/infrastructure/template_loader.py

import os
import sys

def get_template_content(technology_name: str) -> str:
    """
    Retrieves the content of a specific .gitignore template.

    This function is designed to work both in a normal execution and when
    packaged by PyInstaller.

    Args:
        technology_name: The name of the technology (e.g., 'Python', 'Node').

    Returns:
        The content of the corresponding .gitignore file as a string.

    Raises:
        FileNotFoundError: If the template file cannot be found.
        OSError: If there is an error reading the file (e.g., permissions).
    """
    if getattr(sys, 'frozen', False):
        # Running in a PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running in a normal Python environment
        base_path = os.path.dirname(os.path.abspath(__file__))

    template_path = os.path.join(base_path, 'templates', f"{technology_name}.gitignore")

    # Let this raise FileNotFoundError or OSError if it fails.
    # The UI layer will be responsible for catching it.
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()
