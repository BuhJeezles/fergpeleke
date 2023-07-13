class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # create a string variable to record longest unique substring thus far
        longest = 0
        # create a variable to record current substring length (recalculates after reaching a repeated character)
        curr = 0
        # create a dictionary/hashtable to record the characters in the current substring, which will check if characters have been repeated (kv pair = character : index)
        subChars = {}
        # variable for last repeating index
        lastRep = 0

        # iterate through string (s)
        for i in range(len(s)):
            # if character is repeated, find length from last repeated index to current index
            if subChars.get(s[i]) != None:
                if lastRep < subChars.get(s[i]):
                    lastRep = subChars.get(s[i])
                curr = i - lastRep
                subChars[s[i]] = i

            # otherwise, record index of current character and increment curr by 1
            else:
                subChars[s[i]] = i
                curr += 1

            if curr > longest:
                longest = curr

        return longest
