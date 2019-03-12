from survey import AnnonymouseSurvey
import unittest

class TestAnonmousSurvey(unittest.TestCase):

	def setUp(self):
		question = "What languages do you know?"
		self.my_survey = AnnonymouseSurvey(question)
		self.responses = ['English', 'Italian', 'Japanese']


	def test_store_single_response(self):
		self.my_survey.store_response(self.responses[0])

		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_multiple_responses(self):

		for response in self.responses:
			self.my_survey.store_response(response)

		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

unittest.main()
