import random

def quicksort_in_place(arr):

	def sorting(lower, upper):
		# base case: the input indices are the same (1 number)
		if lower == upper:
			return


		# choose a random pivot and swap with the end
		pivIndex = random.randint(lower, upper)
		print(arr)
		print('pivot:', pivIndex, arr[pivIndex])
		print('upper:', upper, arr[upper])
		arr[pivIndex], arr[upper] = arr[upper], arr[pivIndex]
		pivIndex, upper = upper, pivIndex
		print('pivot:', pivIndex,arr[pivIndex])
		print('upper:', upper,arr[upper])
		print(arr)


		# compare # at lower pointer to the pivot
		# if arr[lower] is larger than the pivot, start incrementing upper by -1
		while arr[lower] < arr[pivIndex]:
			lower += 1
		print(arr[pivIndex], arr[lower], arr[upper])


		while arr[upper] > arr[pivIndex]:
			upper -= 1
		print(arr[pivIndex], arr[lower], arr[upper])

		# if lower and upper meet, swap with the pivot and recurse on right and left sides
		if lower == upper:
			arr[pivIndex], arr[upper] = arr[upper], arr[pivIndex]
			upper, pivIndex = pivIndex, upper

			# recurse on the right side
			sorting(pivIndex + 1, upper)
			# recurse on the left side
			sorting(lower, pivIndex - 1)
		
		#swap lower and upper
		else:
			arr[upper], arr[lower] = arr[lower], arr[upper]

	


	sorting(0, len(arr)-1)
	return arr



testArr = [2,1,4,3,6,8]
quicksort_in_place(testArr)
print('-----',testArr)
			# increment left til arr[lower] > pivot
				# increment right til arr[upper] < pivot
					# swap lower and upper

		# swap pivot with index where lower == upper

	#	 recurse on the left and right halves