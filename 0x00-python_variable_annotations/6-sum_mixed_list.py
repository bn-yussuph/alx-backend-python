#!/usr/bin/env python3

"""
A function that takes a list of ints and floats, and return their sum.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
	"""
	Parameters
		input_list: a list of int and floats

	Return: 
		their sum as a float
	"""

	return sum(mxd_lst)
