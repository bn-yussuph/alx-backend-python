#!/usr/bin/env python3
"""A function that takes a list of floats and return their sum"""

from typing import List


def sum_list(input_list: List[float])-> float:
	"""
	Parameters
		input_list: a list of floats

	Return: their sum as a float
	"""

	return float(sum(input_list))
