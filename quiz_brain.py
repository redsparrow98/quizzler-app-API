import html
# HTML module is used to escape the formating of HTML entities in an API response or any text that uses HTML
# It has a method html.unescape()


class QuizBrain:
    def __init__(self, q_list):
        """
        - Initialises the Object with the number of the question being asked.
        - sets the score to 0.
        - creates a question list using a parameter in a form of a dictionary.
        - Sets the current question to None as a start

        :param q_list: Database of questions being asked in the form of a dictionary. Received from API response
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
        - Checks if the question number is smaller than the questions_list database if true it means there are more
        questions to go through and the quizz can keep playing

        :return: True or False for more questions in a list
        """
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

    def check_answer(self, user_answer):
        """
        - Checks the User answer for the question against the correct answer in the Questions database.
        - If right increases the score by 1 and return True
        - If wrong return False

        :param user_answer: The user input After a question is asked
        :return: True or False
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
