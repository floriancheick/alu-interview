#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the pascal's  triangle of n:

Return an empty list if n <= 0 
Your can assume n will be always an integer
"""

def pascal_triangle(n):
	if n <= 0:
		return []
	pascal = [[1]]
	for item in range(n-1):
		pascal.append([i+j for i, j in zip([0] +pascal[-1], pascal[-1] + [0])])
	return pascal
