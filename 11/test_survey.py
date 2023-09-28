import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for class AnonymousSurvey"""

    def setUp(self) -> None:
        """Makes survey for all tests methods"""
        question: str = 'What language did you first learn to speak'
        self.my_survey = AnonymousSurvey(question)
        self.responses: list = ['English', 'Mali', 'Sales']

    def test_store_single_response(self):
        """Check correct save single question"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """three answers correct checking"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

    if __name__ == '__main__':
        unittest.main()
