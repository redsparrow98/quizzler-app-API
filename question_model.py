class Question:
    def __init__(self, q_text, q_answer):
        """
        Question object is initialized using two arguments of str data type, creating the two attributes for the Object

        :param q_text: Thext of the question
        :param q_answer: Correct answer to the question
        """
        self.text = q_text
        self.answer = q_answer
