import unittest
from name_functions import get_formated_name

class NameTestClass (unittest.TestCase):
	'''tests for name_function.py'''

	def test_first_last_name(self):
		'''test for just a firs and last name '''
		formatted_name = get_formated_name('jannis', 'botha')
		self.assertEqual(formatted_name, 'Jannis Botha')

	def test_first_middle_last_name(self):
		''' test to see if a full name with middle name works '''
		formatted_name = get_formated_name('james', 'hunt', 'william')
		self.assertEqual(formatted_name, 'James William Hunt')

unittest.main()