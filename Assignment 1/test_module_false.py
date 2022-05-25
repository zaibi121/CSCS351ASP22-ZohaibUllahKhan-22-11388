import unittest
import code

class test_module_false(unittest.TestCase):

	def test_palindrome_false(self):
		result = code.palindrome("abca")
		self.assertFalse(result,True)

if __name__ == '__main__':
	unittest.main()