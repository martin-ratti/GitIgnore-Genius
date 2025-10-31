# src/infrastructure/template_loader.py

import os
import sys

def get_template_content(technology_name: str) -> str:
    """
    Retrieves the content of a specific .gitignore template.

    Looks for the template file inside the 'templates' directory. This function
    is designed to work both in a normal execution and when packaged by
    PyInstaller.

    Args:
        technology_name: The name of the technology (e.g., 'Python', 'Node').

    Returns:
        The content of the corresponding .gitignore file as a string.
        Returns an error message string if the file is not found.
    """
    try:
        # Determine the base path, accounting for PyInstaller's temporary folder
        if getattr(sys, 'frozen', False):
            # Running in a bundle
            base_path = sys._MEIPASS
        else:
            # Running in a normal Python environment
            base_path = os.path.dirname(os.path.abspath(__file__))

        template_path = os.path.join(base_path, 'templates', f"{technology_name}.gitignore")

        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"# ERROR: Template for '{technology_name}' not found.\n"
    except Exception as e:
        return f"# ERROR: Could not read template for '{technology_name}': {e}\n"