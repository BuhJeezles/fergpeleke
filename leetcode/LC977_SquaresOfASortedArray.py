class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

# easy solution

        #sqNums = [i**2 for i in nums]
        #sqNums.sort()

        #return sqNums



# harder solution, more universally usable for larger datasets

        totalLength = len(nums)
        lPointer = 0
        rPointer = totalLength - 1
        outputArray = [None] * totalLength


        for i in range(totalLength):
            lVal = nums[lPointer] ** 2
            rVal = nums[rPointer] ** 2
            if  lVal <= rVal:
                outputArray[totalLength - i -1] = rVal
                rPointer -= 1
            else:
                outputArray[totalLength - i -1] = lVal
                lPointer += 1

        return outputArray