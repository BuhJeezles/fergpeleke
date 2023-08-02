import BaseSorter.py
'''
MergeSorter implements the BaseSorter interface class using a recursive
implementation of the mergesort algorithm.
'''

class MergeSorter(BaseSorter):
	'''
	Implements recursive mergesort not-in-place on the provided list of ints.
	Abstract function representing a sort operation on a List of integers.


	Args:
		my_list: List[int] of integers, to be sorted in-place.

	Returns:
		None
	'''

	def sort(my_list):
		