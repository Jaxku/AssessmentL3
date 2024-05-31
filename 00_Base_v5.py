import requests
import tkinter as tk
from tkinter import Canvas, Label, StringVar, messagebox, Radiobutton
import os
import tkinter.filedialog
import tkinter.messagebox
from tkinter import simpledialog


# Fetching the questions from the provided URL
parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://raw.githubusercontent.com/Jaxku/AssessmentL3/main/RawQuestionData.json", params=parameters)
question_data = response.json()["results"]

class Question:
    def __init__(self, question, correct_answer, choices):
        self.question = question
        self.correct_answer = correct_answer
        self.choices = choices

class QuizOperation:
    def __init__(self, questions):
        # Initialize the quiz operation with a list of questions.
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def anymore_questions(self):
        # Check if there are more questions in the quiz.
        return self.question_no < len(self.questions)

    def next_question(self):
        # Get the next question in the quiz.
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        return f"Q.{self.question_no}: {self.current_question.question}"

    def check_answer(self, user_answer):
        # Check if the user's answer is correct.
        correct_answer = self.current_question.correct_answer
        return user_answer.lower() == correct_answer.lower()

    def get_score(self):
        # Get the final score.
        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return self.score, wrong, score_percent


class QuizGUI:

    def __init__(self, quiz):
        # Initialize the Quiz GUI.
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("Maori Quiz!")
        self.window.geometry("800x600")

        self.user_answer = StringVar()
        self.opts = []

        self.display_title()
        self.canvas = Canvas(self.window, width=800, height=250)
        self.canvas.create_text(400, 125, text="Question", width=680, fill="black", font=('Arial', 15, 'bold'), tag="question")
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)

        self.display_question()
        self.radio_buttons()
        self.display_options()

        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.grid(row=5, column=0, columnspan=2)

        self.buttons()
        self.window.mainloop()

    def display_title(self):
        # Display the title of the quiz application.
        title = Label(self.window, text="Maori Quiz", width=50, bg="Red", fg="white", font=("ariel", 20, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=10)

    def display_question(self):
        # Display the next question on the canvas.
        self.canvas.delete("question")
        q_text = self.quiz.next_question()
        self.canvas.create_text(400, 80, text=q_text, width=680, fill="black", font=('Arial', 15, 'bold'), tag="question")

    def radio_buttons(self):
        # Create radio buttons for the quiz options.
        y_pos = 220
        for _ in range(4):
            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer, value='', font=("ariel", 14))
            radio_btn.place(x=200, y=y_pos)
            self.opts.append(radio_btn)
            y_pos += 40

    def display_options(self):
        # Display the options (possible answers) for the current question.
        self.user_answer.set(None)
        for rb in self.opts:
            rb.deselect()

        choices = self.quiz.current_question.choices
        for i, choice in enumerate(choices):
            self.opts[i].config(text=choice, value=choice)

    def buttons(self):
        # Create the Next and Quit buttons.
        next_button = tk.Button(self.window, text="Next", command=self.check_answer)
        next_button.grid(row=6, column=1, pady=20)

        quit_button = tk.Button(self.window, text="Quit", command=self.window.destroy)
        quit_button.grid(row=6, column=0, pady=20)

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




# Create questions from the question_data
questions = []
for item in question_data:
    question = Question(item['question'], item['correct_answer'], item['incorrect_answers'] + [item['correct_answer']])
    questions.append(question)

# Initialize the quiz and GUI
quiz = QuizOperation(questions)
quiz_gui = QuizGUI(quiz)
