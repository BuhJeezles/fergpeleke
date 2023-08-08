'''
Sorting_Test.py
'''

import MergeSorter.py
import BaseSorter.py

'''
Args:
	base_sorter: An instance of a BaseSorter subclass to be tested
	correct_list: The list to be sorted by the base_sorter instance
	answer_list: The correctly sorted list
'''

# creating a list of lists to sort (testing_list) and corresponding correct_list:
# [[empty list], [no repeats], [with repeats], [same number], [already sorted], [backwards order], [negatives no repeat], [negatives w/ repeat]]
testing_list = [[], [5,2,6,3,1,0,4], [2,1,3,1,0,9,4,7,7], [1,1,1,1,1], [0,1,2,3,4,5], [5,4,3,2,1,0], [5,-1,3,-2,-7,0], [7,-1,-3,0,0,4,2,-3,-1]]
correct_list = [[], [0, 1, 2, 3, 4, 5, 6], [0, 1, 1, 2, 3, 4, 7, 7, 9], [1, 1, 1, 1, 1], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [-7, -2, -1, 0, 3, 5], [-3, -3, -1, -1, 0, 0, 2, 4, 7]]


def TestSort(base_sorter, correct_list, answer_list):
  ans = base_sorter.Sort(test_list)
  if ans != correct_list:
  	raise Exception(f"Error! ans {ans}!= correct_list {correct_list}")
    
def TestIsSorted(base_sorter, test_list, answer_bool):
  # Will does things here
  print('placeholder')

def __main__():
	