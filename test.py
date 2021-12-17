#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Gift Tangsupakij
# Date: 12/16/2021
# Description: This file contains test cases of the integerToRoman function

# standard library
import unittest

# local source
import funcs
from funcs import integerToRoman


class TestIntegerToRoman(unittest.TestCase):
    def test_num_not_integer(self):
        """ Test the function with non integer argument """
        try:
            res = integerToRoman('1')
        except AssertionError as err:
            self.assertEqual(err.__str__(), funcs.NON_INT_ERR_MSG)
        else:
            self.assertEqual(res, "I")

    def test_num_zero(self):
        """ Test the function with zero """
        try:
            res = integerToRoman(0)
        except AssertionError as err:
            self.assertEqual(err.__str__(), funcs.OUT_RANGE_ERR_MSG)
        else:
            self.assertEqual(res, "I")

    def test_negative_num(self):
        """ Test the function with negative input number """
        try:
            res = integerToRoman(-5)
        except AssertionError as err:
            self.assertEqual(err.__str__(), funcs.OUT_RANGE_ERR_MSG)
        else:
            self.assertEqual(res, "I")

    def test_num_greater_than_3999(self):
        """ Test the function with input number that is greater than 3999 """
        try:
            res = integerToRoman(4000)
        except AssertionError as err:
            self.assertEqual(err.__str__(), funcs.OUT_RANGE_ERR_MSG)
        else:
            self.assertEqual(res, "I")

    def test_valid_num1(self):
        """
        Test valid number
        23 => XXIII
        """
        num = 23
        out = "XXIII"
        self.assertEqual(integerToRoman(num), out, "{} != {}".format(num, out))

    def test_valid_num2(self):
        """
        Test valid number
        1940 => MCMXL
        """
        num = 1940
        out = "MCMXL"
        self.assertEqual(integerToRoman(num), out, "{} != {}".format(num, out))

    def test_valid_num3(self):
        """
        Test valid number
        44 => XLIV
        """
        num = 44
        out = "XLIV"
        self.assertEqual(integerToRoman(num), out, "{} != {}".format(num, out))

    def test_valid_num4(self):
        """
        Test valid number
        457 => CDLVII
        """
        num = 457
        out = "CDLVII"
        self.assertEqual(integerToRoman(num), out, "{} != {}".format(num, out))

    def test_valid_num5(self):
        """
        Test valid number
        3999 => MMMCMXCIX
        """
        num = 3999
        out = "MMMCMXCIX"
        self.assertEqual(integerToRoman(num), out, "{} != {}".format(num, out))

    def test_valid_num6(self):
        """
        Test valid number
        1 => I
        """
        num = 1
        out = "I"
        self.assertEqual(integerToRoman(num), out, "{} != {}".format(num, out))

    def test_valid_num7(self):
        """
        Test valid number
        2560 => MMDLX
        """
        num = 2560
        out = "MMDLX"
        self.assertEqual(integerToRoman(num), out, "{} != {}".format(num, out))

    def test_valid_num8(self):
        """
        Test valid number
        732 => DCCXXXII
        """
        num = 732
        out = "DCCXXXII"
        self.assertEqual(integerToRoman(num), out, "{} != {}".format(num, out))


if __name__ == '__main__':
    unittest.main()
