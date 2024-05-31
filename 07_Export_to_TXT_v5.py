"""
puts user in loop to save or abort, also locks test so the result cant be altered (bug fix)
"""


import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox as messagebox
from tkinter import simpledialog


def export_score_high_score(self, score):
    # Export function to record the score and user's name in a text file.
    user_name = simpledialog.askstring("Enter Username", "Please enter your username:")

    if user_name:
        while True:
            # Asking the user to select a location to save the file
            save_path = tk.filedialog.askdirectory(title="Select Folder to Save Your Score")

            if save_path:
                # Creating the file name and path
                file_name = f"{user_name}_score.txt"
                file_path = os.path.join(save_path, file_name)

                # Writing the score to the file
                with open(file_path, "w") as file:
                    file.write(f"User: {user_name}\n")
                    file.write(f"Score: {score}\n")

                # Displaying message box with confirmation
                messagebox.showinfo("Score Saved", f"Score saved successfully for {user_name}!")

                # Ending the program
                self.window.destroy()
                break
            else:
                # Ask if the user wants to abort saving
                if messagebox.askyesno("Error", "No folder selected! Do you want to abort saving?"):
                    confirm_abort = messagebox.askyesno("Confirm Abort", "Are you sure you want to abort saving the score?")
                    if confirm_abort:
                        # End the program if the user confirms aborting
                        self.window.destroy()
                        break
    else:
        # Displaying an error message if no username is provided
        messagebox.showerror("Error", "Username cannot be empty!")

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
