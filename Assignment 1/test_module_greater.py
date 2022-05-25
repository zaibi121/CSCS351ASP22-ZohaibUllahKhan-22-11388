import unittest
import code

class test_module_greater(unittest.TestCase):

	def test_power_greater(self):
		result = code.take_power(2,2)
		self.assertGreater(result,3)

if __name__ == '__main__':
	unittest.main()