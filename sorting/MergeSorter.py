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
		midpoint = listLen // 2

		# recurse until we have len == 1
		if len(my_list) <= 1:
			return

		left = my_list[:midpoint]
		right = my_list[midpoint:]

		left = sort(left)
		right = sort(right)

		# combining left and right subsections
		combinedList = []
		rightIndex = 0
		leftIndex = 0

		while True:
			if leftIndex < len(left) and rightIndex < len(right):
				if left[leftIndex] < right[rightIndex]:
					combinedList.append(left[leftIndex])
					leftIndex += 1
				else:
					combinedList.append(right[rightIndex])
					rightIndex += 1
			elif leftIndex < len(left):
				combinedList.append(left[leftIndex])
			elif rightIndex < len(right):
				combinedList.append(right[rightIndex])
			else:
				return combinedList





