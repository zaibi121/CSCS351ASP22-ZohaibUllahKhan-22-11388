import unittest
import code

class test_module_true(unittest.TestCase):

	def test_palindrome_true(self):
		result = code.palindrome("abba")
		self.assertTrue(result,False)

if __name__ == '__main__':
	unittest.main()