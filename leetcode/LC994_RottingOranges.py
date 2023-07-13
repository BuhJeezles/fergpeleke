from collections import deque

class Solution:
    '''
    solution for LC994 - Rotting oranges
    Given an array of:
        0: empty cell
        1: fresh orange
        2: rotten orange

        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
        Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
    '''
    
    def orangesRotting(self, grid):

        class OrangeDist:
            '''
            helper class to record orange coordinates and distance from rotten
            '''
            def __init__(self, row, col, dist = 0):
                self.col = col
                self.row = row
                self.dist = dist

            def __str__(self):
                return f" row: {self.row}, col:{self.col}, dist: {self.dist}============="

            

        maxRow = len(grid)
        maxCol = len(grid[0])

        # helper to check if coordinates are valid
        def inBounds(stupidOrange):
            if (stupidOrange.row < maxRow and stupidOrange.row >= 0) and \
            (stupidOrange.col < maxCol and stupidOrange.col >= 0):
                return True
            return False
        

        fresh = set()
        BFSqueue = deque()


        # array of 0's and 1's denoting whether a box has been traversed
        traversed = [[0] * maxCol for i in range(maxRow)]


        #### come back to this if this breaks
        # create a set for all the coordinates for 1's (where 0 = empty space, 1 = fresh orange, 2 = rotten orange)
        for i in range(maxRow):
            for j in range(maxCol):
                if grid[i][j] == 1:
                    fresh.add((i,j))


        # queue for all the 2's
                elif grid[i][j] == 2:
                    BFSqueue.append(OrangeDist(i,j,0))
                    traversed[i][j] = 1

        
        # if there are no fresh ones to begin with
        if len(fresh) == 0:
            return 0


        # perform BFS
        cardDir = [(-1,0), (1,0), (0,-1), (0,1)]


        # variable to store largest distance thus far
        largestDist = 0


        while len(BFSqueue) > 0:
            currOrange = BFSqueue.popleft()


            for i in cardDir:
                neighborOrange = OrangeDist(i[0] + currOrange.row, i[1] + currOrange.col, currOrange.dist + 1)


                # conditions: within boundaries, not traversed, and not a zero
                if inBounds(neighborOrange):
                    if traversed[neighborOrange.row][neighborOrange.col] != 1:
                        if grid[neighborOrange.row][neighborOrange.col] != 0:

                            # add to queue
                            BFSqueue.append(neighborOrange)

                            # update the traversed 
                            traversed[neighborOrange.row][neighborOrange.col] = 1

                            # remove from fresh set
                            fresh.remove((neighborOrange.row, neighborOrange.col))

                            # update largest distance if applicable
                            if neighborOrange.dist > largestDist:
                                largestDist = neighborOrange.dist

        if len(fresh) > 0:
            return -1
        return largestDist