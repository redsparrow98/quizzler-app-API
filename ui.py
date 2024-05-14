from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 14, "italic")


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        """
        Initialises a GUI for the quizz game, passes in the QuizBrain Class, so the methods can be used in the GUI:

        - Quiz for the QuizBrain
        - window
        - canvas for questions
        - score label
        - True Button answer
        - False button answer
        """
        self.quiz = quiz_brain

        # window
        self.window = Tk()
        self.window.title("Quizz-game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score label
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # Canvas for question
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        # to wrap text to canvas, we use width argument setting the max length of a text before wrapping
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
            command=self.true_pressed
            )
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_img,
            highlightthickness=0,
            command=self.false_pressed
            )
        self.false_button.grid(column=1, row=2)

        # gets the question to update the canvas has to be called before the mainloop, so it would update
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """
        - Method updates the canvas background color to white since it might be red or green if already answering
        questions.
        - Checks if the quiz brain has more question by calling the quizz still_has_questions method if true updates
        question and canvas accordingly, also disables the buttons from being pressed again.
        - if false updates canvas text to let user know it's the end of quizz
        - Sets The score label to the quiz brain score that gets updated as the player plays the game
        - Calls on to the QuizzBrain next question to get the question from the API and updates the canvas on the
        GUI to what the current question is.

        :return: The current question being asked from the QuizBrain
        """
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.question_txt, text=question_txt)
        else:
            self.canvas.itemconfig(self.question_txt, text="You've reached the end of the quiz")
            # setting the state of the button to disabled makes the buttons not pressable
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """
        - Method calls on to the quiz brain method Check answer while passing "True" as the user answers.
        - This method checks if the answer is correct or not in the form of bool and saves it in the is_right var.
        - The is_right var gets passed in to the give feedback method that updates the canvas colort to green or red as
        a visual que to the user.

        :return: True or False for the answer
        """
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        """
        - Method calls on to the quiz brain method Check answer while passing "False" as the user answers.
        - This method checks if the answer is correct or not in the form of bool and saves it in the is_right var.
        - The is_right var gets passed in to the give feedback method that updates the canvas colort to green or red as
        a visual que to the user.

        :return: True or False for the answer
        """
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """
        - Method takes the is_right argument and checks for True or False.
        - If True, updates the canvas color to green
        - If False, updates the canvas color to red

        - After a second pass, the get_next question gets called reseting the canvas to white and putting in a
        new question.

        :param is_right: True or False Bool
        :return: Color of canvas change depending on correctness of answer and updates new question after 1s
        """
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
