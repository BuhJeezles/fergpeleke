class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        '''
        no return, just modify nums in-place
        '''

        # cheating answer using builtin stuff (don't do this in jobs)
        '''
            firstIndex = 0
            lastIndex = len(nums) - 1

            while firstIndex + 1 <= lastIndex:
                if nums[firstIndex] == 0:
                    nums.append(nums.pop(firstIndex))
                    lastIndex -= 1
                else:
                    firstIndex += 1
        '''

        # create variable storing index of first zero (tempVar)
        tempVar = None

        # iterate thru nums
        for i in range(len(nums)):
            if nums[i] == 0 and tempVar == None:
                    tempVar = i
            elif nums[i] != 0 and tempVar != None:
                nums[tempVar], nums[i] = nums[i], nums[tempVar]
                tempVar += 1
