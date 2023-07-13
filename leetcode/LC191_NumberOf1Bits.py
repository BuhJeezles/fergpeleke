class Solution:
    def hammingWeight(self, n: int) -> int:
        oneCount = 0
        for i in bin(n):
            if i == "1":
                oneCount += 1

        return oneCount
