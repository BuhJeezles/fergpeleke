class Solution:
    def isPowerOfTwo(self, n: int) -> bool: 
        tempNum = n

        while tempNum > 2:
            tempNum = tempNum / 2

        if tempNum == 2 or tempNum == 1:
            return True

        return False



'''


'''