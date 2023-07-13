class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
        O(n^2) ?
        '''
        ans = []
        numSize = len(nums)
        startArr = []

        def findPermutation(currArr):
            # base case: current array is the same size as initial input array
            if len(currArr) == numSize:     # O(1)
                ans.append(currArr.copy())
                return
            # do work
            for i in nums:                  # O(n)
                if i not in currArr:        # O(m)        
                    # could also use a second SET depending on the size of the array; whether we want faster or less space usage
                    currArr.append(i)               
                    findPermutation(currArr)
                    currArr.pop()                   # removes last item and goes to the next item       [1,2,3,4]  pop  [1,2,3]  pop  [1,2]  add  [1,2,4]  add  [1,2,4,3]

        findPermutation(startArr)

        return ans