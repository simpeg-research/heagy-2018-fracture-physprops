import os
import numpy as np
import testipynb
import unittest

NBDIR = os.path.sep.join(
    os.path.abspath(__file__).split(os.path.sep)[:-2] + ['notebooks']
)

IGNORE = []

Test = testipynb.TestNotebooks(directory=NBDIR, timeout=2800)
test_nbnames = [t for t in Test._nbnames if t not in IGNORE]
Test.ignore = IGNORE
TestNotebooks = Test.get_tests()

if __name__ == "__main__":
    unittest.main()
