import unittest
import code

class test_module_notequal(unittest.TestCase):

	def test_power_notequal(self):
		result = code.take_power(2,2)
		self.assertNotEqual(result,3)

if __name__ == '__main__':
	unittest.main()
