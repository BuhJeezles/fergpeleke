# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left, right = 0, n
        lastGood = 0
        firstBad = 0

        while (lastGood + 1) != firstBad:
            mid = (left + right) // 2
            if isBadVersion(mid):
                firstBad = mid
                right = mid - 1
            
            else:
                lastGood = mid
                left = mid + 1

        return firstBad