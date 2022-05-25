import unittest
import code

class test_module_equal(unittest.TestCase):

	def test_power_equal(self):
		result = code.take_power(2,2)
		self.assertEqual(result,4)


if __name__ == '__main__':
	unittest.main()
