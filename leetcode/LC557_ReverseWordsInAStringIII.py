class Solution:
    def reverseWords(self, s: str) -> str:

        wordList = s.split()
        output = ""

        for i in range(len(wordList)):
            revWord = wordList[i][::-1]
            output += revWord

            if i != len(wordList) - 1:
                output += " "

        return output
        