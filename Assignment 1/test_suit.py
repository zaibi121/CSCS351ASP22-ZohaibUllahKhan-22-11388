import unittest

import test_module_equal
import test_module_notequal
import test_module_greater
import test_module_less
import test_module_true
import test_module_false

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_module_equal))
suite.addTests(loader.loadTestsFromModule(test_module_notequal))
suite.addTests(loader.loadTestsFromModule(test_module_greater))
suite.addTests(loader.loadTestsFromModule(test_module_less))
suite.addTests(loader.loadTestsFromModule(test_module_true))
suite.addTests(loader.loadTestsFromModule(test_module_false))


# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)


