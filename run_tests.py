import unittest
import sys
import os

# Ensure current directory is in path
sys.path.append(os.getcwd())

from tests import test_rules, test_engine

suite = unittest.TestSuite()
suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_rules))
suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_engine))

runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
result = runner.run(suite)

if not result.wasSuccessful():
    sys.exit(1)
