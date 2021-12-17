#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Gift Tangsupakij
# Date: 12/16/2021
# Description: This file contains a function that converts integers to Roman numerals


# Error messages
NON_INT_ERR_MSG = "Input number must be an integer"
OUT_RANGE_ERR_MSG = "Input number must be greater than zero and less than 4000"


def integerToRoman(num: int) -> str:
    """
    Converts a positive integer number to a roman numeral
    :param num: A positive integer, num > 0
    :return: A string represents Roman numeral
    """

    assert isinstance(num, int), NON_INT_ERR_MSG
    assert 0 < num < 4000, OUT_RANGE_ERR_MSG

    numeralMap = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    out = ""

    for k, v in numeralMap.items():
        digit, num = divmod(num, k)
        out += v * digit

    return out
