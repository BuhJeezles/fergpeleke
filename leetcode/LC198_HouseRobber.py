class Solution:
    def rob(self, nums: List[int]) -> int:
        # take array as input
        def chooseHouses(arr):
            # base case: array is size 0
            if len(arr) == 0:
                return 0

            # base case: array is size 1:
            if len(arr) == 1:
                return arr[0]

            # base case: array is size 2:
            if len(arr) == 2:
                return max(arr[0], arr[1])

            # find indices for left and right subarrays
            midIndex = len(arr) // 2

            # choose left to skip
            leftSkipLeft = chooseHouses(arr[0 : midIndex])                  # skipping mid index because python shenanigans; this is the left subarr
            rightSkipLeft = chooseHouses(arr[midIndex+1 : len(arr)])        # skipping mid index; this is the right subarr

            # choose right to skip
            leftSkipRight = chooseHouses(arr[0 : midIndex+1])
            rightSkipRight = chooseHouses(arr[midIndex+2 : len(arr)])

            totalSkipLeft = leftSkipLeft + rightSkipLeft
            totalSkipRight = leftSkipRight + rightSkipRight
            totalSkipBoth = leftSkipLeft + rightSkipRight

            # compare which is largest and return
            return max(totalSkipLeft, totalSkipRight, totalSkipBoth)

        return chooseHouses(nums)