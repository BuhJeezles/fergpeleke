class Solution:
    def climbStairs(self, n: int) -> int:
        import math

        firstTwoCount = n // 2
        if n % 2 == 0:
            firstOneCount = 0
        else:
            firstOneCount = 1
    
        # initializing a counter to count the number of ways steps can be climbed (permutations)
        self.count = 0

        def permutationCounter(oneCount, twoCount):
            '''
            Takes the number of ones, and number of twos in the current combination of 1s and 2s,
            and finds the number of permutations. Starting combination is max number of 2's
            Args:
                oneCount [int]: number of ones in the current combination of 1's and 2's
                twoCount [int]: number of twos ^
            Returns:
                oneCount, twoCount: but updated with replacing a 2 with two 1's
            '''
            # base case: if we've gone down to all ones
            if twoCount == 0:
                self.count += 1
                return

            # equation for number of permutations with repeats (n! / n1!n2!...nz!)
            self.count += math.factorial(oneCount + twoCount) / (math.factorial(oneCount) * math.factorial(twoCount))
            oneCount += 2
            twoCount -= 1

            return permutationCounter(oneCount, twoCount)

        permutationCounter(firstOneCount, firstTwoCount)

        return int(self.count)