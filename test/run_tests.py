"""This module uses unittest TestLoader to run tests"""
import sys
import unittest

if __name__ == '__main__':
    sys.dont_write_bytecode = True
    SUITE = unittest.TestLoader().discover(".")
    unittest.TextTestRunner(verbosity=1, buffer=True).run(SUITE)
