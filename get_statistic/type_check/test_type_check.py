import unittest
from get_statistic.type_check import type_check
from argparse import ArgumentTypeError


class TestTypeCheck(unittest.TestCase):

    def test_check_positive(self):
        """
            check_positive should return only positive int number
        """
        test_cases_positive = ['4', '8', '15', '16', '23', '42']
        for case in test_cases_positive:
            self.assertEqual(type_check.check_positive(case), int(case), [
                'check_positive should return int if number is positive'])
        test_cases_negative = ['-4', '-8', '-15', '-16', '-23', '-42']
        for case in test_cases_negative:
            with self.assertRaises(ArgumentTypeError):
                # check_positive should raise error if number is negative
                type_check.check_positive(case)

        with self.assertRaises(ArgumentTypeError):
            # check_positive should raise error if number is 0
            type_check.check_positive('0')
