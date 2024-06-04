"""
puts user in loop to save or abort, also locks test so the result cant be altered (bug fix)
"""


import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox as messagebox
from tkinter import simpledialog


def export_score_high_score(self, score):
        """Export the user's score to a text file."""
        while True:
            # Ask for the user's name
            user_name = simpledialog.askstring(
                "Enter Username", "Please enter your username:"
            )

            # If user presses Cancel, ask if they want to abort saving
            if user_name is None:
                if messagebox.askyesno(
                    "Confirm Abort",
                    "You pressed cancel. Do you want to abort saving the score?"
                ):
                    try:
                        self.window.destroy()
                    except tk.TclError:
                        pass
                    return  # Exit the function

            # If the username is empty, show an error and continue the loop
            elif not user_name.strip():
                messagebox.showerror(
                    "Error",
                    "Username cannot be empty. Please enter your username."
                )

            # If a valid username is entered
            else:
                while True:
                    # Ask the user to select a location to save the file
                    save_path = tk.filedialog.askdirectory(
                        title="Select Folder to Save Your Score"
                    )

                    # If a valid folder is selected
                    if save_path:
                        # Create the file name and path
                        file_name = f"{user_name}_score.txt"
                        file_path = os.path.join(save_path, file_name)

                        # Write the score to the file
                        with open(file_path, "w") as file:
                            file.write(f"User: {user_name}\n")
                            file.write(f"Score: {score}\n")

                        # Display confirmation message
                        messagebox.showinfo(
                            "Score Saved",
                            f"Score saved successfully for {user_name}!"
                        )

                        # End the program
                        try:
                            self.window.destroy()
                        except tk.TclError:
                            pass
                        return  # Exit the function

                    # If no folder is selected, ask if the user wants to abort saving
                    else:
                        if messagebox.askyesno(
                            "Error",
                            "No folder selected! Do you want to abort saving?"
                        ):
                            if messagebox.askyesno(
                                "Confirm Abort",
                                "Do you want to abort saving the score?"
                            ):
                                try:
                                    self.window.destroy()
                                except tk.TclError:
                                    pass
                                return  # Exit the function


def check_answer(self):
    # Check the user's answer and update the quiz state.
    selected_answer = self.user_answer.get()
    if self.quiz.check_answer(selected_answer):
        self.quiz.score += 1
        self.feedback.config(text="Correct!", fg="green")
    else:
        self.feedback.config(text="Wrong!", fg="red")

    if self.quiz.anymore_questions():
        self.display_question()
        self.display_options()
    else:
        score, wrong, percent = self.quiz.get_score()
        self.feedback.config(text=f"Quiz Ended!\nScore: {score}/{self.quiz.question_no}\nWrong: {wrong}\nPercent: {percent}%")
        self.export_score_high_score(score)
        self.lock_quiz()


def lock_quiz(self):
    # Lock the quiz by disabling the Next button
    for btn in self.opts:
        btn.config(state='disabled')
    self.window.children["!button"].config(state='disabled')



# for testing purposes only
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    export_score_high_score(10)
