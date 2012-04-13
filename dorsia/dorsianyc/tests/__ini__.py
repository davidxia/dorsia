import unittest

from dorsianyc.tests import model_tests


def suite():
    tests_loader = unittest.TestLoader().loadTestsFromModule
    test_suites = []
    test_suites.append(tests_loader(field_tests))
    test_suites.append(tests_loader(storage_tests))
    return unittest.TestSuite(test_suites)
