import unittest
import code

class test_module_less(unittest.TestCase):

	def test_power_less(self):
		result = code.take_power(2,2)
		self.assertLess(result,5)

if __name__ == '__main__':
	unittest.main()