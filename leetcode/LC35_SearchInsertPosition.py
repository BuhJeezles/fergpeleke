class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:  

        left, right = 0, len(nums) - 1

        # binary search
        while left != right:
            mid = ((right - left) // 2) + left

            if nums[mid] == target:
                return mid

            elif target < nums[mid]:
                right = mid

            elif target > nums[mid]:
                left = mid + 1

#### if its NOT in there

        if target <= nums[left]:
            return left
        if target > nums[left]:
            return left + 1
            


