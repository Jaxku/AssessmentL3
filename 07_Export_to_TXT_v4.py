"""
Export function adds the addition to use windows explorer to select the save location.
"""


import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox as messagebox
from tkinter import simpledialog


def export_score_high_score(score):

    user_name = simpledialog.askstring\
        ("Enter Username", "Please enter your username:")

    if user_name:
        # Asking the user to select a location to save the file
        save_path = tk.filedialog.askdirectory\
            (title="Select Folder to Save Your Score")

        if save_path:
            # Creating the file name and path
            file_name = f"{user_name}_score.txt"
            file_path = os.path.join(save_path, file_name)
            # Using the selected folder to save the file

            # Checking if the file exists and reading the current high score
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    high_score = int(file.readline().split(":")[-1].strip())
            else:
                high_score = 0

            # Comparing current score with high score
            if score > high_score:
                # Writing new high score to the file
                with open(file_path, "w") as file:
                    file.write(f"User: {user_name}\n")
                    file.write(f"Score: {score}\n")
                # Displaying message box with congratulations
                messagebox.showinfo\
                    ("High Score", f"Congratulations {user_name}! "
                                   f"You achieved a new high score: {score}")
            else:
                # Displaying message box with current score
                messagebox.showinfo\
                    ("High Score", f"Your score: {score}"
                                   f"\nCurrent high score: {high_score}")
        else:
            # Displaying an error message if no folder is selected
            messagebox.showerror("Error", "No folder selected! "
                                          "Score not saved.")
    else:
        # Displaying an error message if no username is provided
        messagebox.showerror("Error", "Username cannot be empty!")


# for testing purposes only
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    export_score_high_score(10)
