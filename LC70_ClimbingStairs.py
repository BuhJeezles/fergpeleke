class Solution:
    def climbStairs(self, n):

        def fibonacci(inputNum):
            # base case: 1 stair
            if inputNum == 1:
                return 1
            # base case: 2 stairs
            if inputNum == 2:
                return 2

            ret = fibonacci(inputNum - 1) + fibonacci(inputNum - 2)

            return ret

        
        return fibonacci(n)


test = Solution()
test1 = test.climbStairs(8)
print(test1)