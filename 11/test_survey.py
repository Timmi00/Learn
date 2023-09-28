import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for class AnonymousSurvey"""

    def test_store_single_response(self):
        """Check correct save single question"""
        question: str = 'What language did you first learn to speak'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_response(self):
        """three answers correct checking"""
        question: str = 'What language did you first learn to speak'
        my_survey = AnonymousSurvey(question)
        responses: list = ['English', 'Mali', 'Sales']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

    if __name__ == '__main__':
        unittest.main()
