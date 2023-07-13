class Solution:
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:

        charCount = {}

        # O(n * nlogn)
        charS1 = [i for i in s1]
        charS1.sort()
        s1Len = len(s1)


        for i in range(len(s2) - s1Len + 1):
            
            if s2[i] in charS1:
                charS2 = s2[i:i+s1Len]
                charS2 = [j for j in charS2]
                charS2.sort()

                if charS2 == charS1:
                    return True

        return False
        '''
# do this using a hash map:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create hash table to store counts of characters
        charCount1 = {}
        
        # create an int variable to store the total number of characters; we'll update this later with some cool shenanigans that i'll comment on later
        s1Len = len(s1)
        if s1Len > len(s2):
            return False

        # populate hash table with kv pairs [character : quantity]
        for i in s1:
            # if character doesn't exist in the dictionary, initialize count to 1
            if charCount1.get(i) == None:
                charCount1[i] = 1
            # if character DOES exist, increment count by 1
            else:
                charCount1[i] += 1     

        # initialize a second hash table that stores character counts for "window" of length s1 using first s1Len # of characters in s2
        charCount2 = {}

        for i in range(s1Len):
            if charCount2.get(s2[i]) == None:
                charCount2[s2[i]] = 1
            else:
                charCount2[s2[i]] += 1

        if charCount2 == charCount1:
            return True
        
        # increment window for the remaining characters in s2
        for i in range(s1Len, len(s2)):
            if charCount2.get(s2[i]) == None:
                charCount2[s2[i]] = 1

            else:
                charCount2[s2[i]] += 1

            charCount2[s2[i-s1Len]] -= 1            # dropping character count for lowest index in window
            if charCount2[s2[i-s1Len]] == 0:        # removing key from dictionary
                charCount2.pop(s2[i-s1Len])

            if charCount1 == charCount2:
                return True

        return False
            

            # can rewrite with skipping around stuff using two pointers
            