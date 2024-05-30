"""
Enhanced export function with a prompt to select the export location.
"""

import os
import tkinter as tk
import tkinter.filedialog


def export_score_enhanced(score, user_name):
    file_name = f"{user_name}_score.txt"
    file_path = tk.filedialog.asksaveasfilename\
        (defaultextension=".txt", filetypes=[("Text files", "*.txt")],
         initialfile=file_name, title="Save Score")
    if file_path:
        with open(file_path, "w") as file:
            file.write(f"User: {user_name}\n")
            file.write(f"Score: {score}\n")
