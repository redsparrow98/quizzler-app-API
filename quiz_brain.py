import html
# HTML module is used to escape the formating of HTML entities in an API response or any text that uses HTML
# It has a method html.unescape()


class QuizBrain:

    def __init__(self, q_list):
        """
        Initialises the Object with the number of the question being asked, sets the score to 0,
        creates a question list using a parameter in a form of a dictionary.
        Sets the current question to None as a start

        :param q_list: Database of questions being asked in the form of a dictionary. Received from API response
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        - Sets the current question number and increases by 1 every time a new question is asked.
        - Question text (q_text) is created, and HTML unescape is used to format the API question formating and replace
        all the HTML escape formating.
        - User is asked for input
        - The user input is checked against the correct answer of the question.

        :return: Returns the result of the check_answer method
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        """
        - Checks the User answer for the question against the correct answer in the Questions database.
        - If right increases the score by 1 and lets user know
        - If wrong lets user know
        - displays the user score and question number at the end

        :param user_answer: The user input After a question is asked
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
