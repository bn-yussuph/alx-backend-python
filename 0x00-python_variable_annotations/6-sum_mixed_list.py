#!/usr/bin/env python3
"""A function that takes a list of ints and floats, and return their sum"""

from typing import List


def sum_mixed_list(mxd_lst: List[typing.Union[int, float]]) -> float:
	"""
	Parameters
		input_list: a list of floats

	Return: their sum as a float
	"""

	return sum(mxd_lst)
