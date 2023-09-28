class AnonymousSurvey:
    """Сбор анонимных ответов на вопросы"""

    def __init__(self, question: str):
        """Save question """
        self.question = question
        self.responses = []

    def show_question(self):
        """print question"""
        print(self.question)

    def store_response(self, new_response: str):
        """Save answer"""
        self.responses.append(new_response)

    def show_results(self):
        """Print all answers"""
        print('Survey results:')
        for response in self.responses:
            print(f'- {response}')

