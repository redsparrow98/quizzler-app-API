from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 14, "italic")


class QuizzInterface:
    """
    Initialises a GUI for the quizz game.
    With window, canvas for questions a score label and a True or false buttons for user input answers.
    """

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # window
        self.window = Tk()
        self.window.title("Quizz-game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score label
        self.score_label = Label(text="Score: ", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # Canvas for question
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_txt = self.canvas.create_text(
            150,
            125,
            width=280,
            text="this is a test",
            font=FONT,
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons for true or false
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_img,
            highlightthickness=0,
            )
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_img,
            highlightthickness=0,
            )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question_txt = self.quiz.next_question()
        self.canvas.itemconfig(self.question_txt, text=question_txt)

