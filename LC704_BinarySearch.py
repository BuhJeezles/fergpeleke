
class Solution:

    def search(self, nums: list[int], target: int) -> int:
        lboundary = 0
        rboundary = len(nums)-1
        mid = int()

        while lboundary <= rboundary:

            mid = (lboundary + rboundary)//2

            if target == nums[mid]:
                return mid
                
            elif target < nums[mid]:
                rboundary = mid - 1

            elif target > nums[mid]: 
                lboundary = mid + 1

        
        return -1