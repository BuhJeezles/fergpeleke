class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tempSet = set()
        for i in nums:
            if i in tempSet:
                tempSet.remove(i)
            else:
                tempSet.add(i)
        return tempSet.pop()