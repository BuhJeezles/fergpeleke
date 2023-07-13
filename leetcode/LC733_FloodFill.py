class Solution(object):
    def floodFill(self,image, sr, sc, color):

        pixelStack = deque()        # queue containing pixels to traverse
        pixelStack.append((sr,sc))  # adding the input pixel to the queue
        travSet = set()             # set containing the pixels traversed (sets in python are implemented as hashtables, so O(n) retrieval time)

        maxRow = len(image)
        maxCol = len(image[0])

        # helper function to determine if an item is in the grid boundaries
        def inBoundary(rowIndex, colIndex):
            if rowIndex >= 0 and rowIndex < maxRow:
                if colIndex >= 0 and colIndex < maxCol:
                    return True
            return False


        origColor = image[sr][sc]


        while len(pixelStack) > 0:
            srCurr, scCurr = pixelStack.pop()
            image[srCurr][scCurr] = color
            travSet.add((srCurr, scCurr))


            north = (srCurr - 1, scCurr)
            south = (srCurr + 1, scCurr)
            east = (srCurr, scCurr + 1)
            west = (srCurr, scCurr - 1)

            cardDir = [north, south, east, west]

            for i in cardDir:
                if inBoundary(i[0],i[1]) and (image[i[0]][i[1]] == origColor) and ((i[0], i[1]) not in travSet):
                    pixelStack.append((i))


        return image