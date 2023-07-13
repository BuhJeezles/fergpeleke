from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:\


        maxRow = len(mat)
        maxCol = len(mat[0])


        # helper function to determine if coordinates are within boundaries
        def inBounds(coordsTuple):
            if (coordsTuple[0] < maxRow and coordsTuple[0] >= 0) and (coordsTuple[1] < maxCol and coordsTuple[1] >= 0):
                return True
            return False


        # initializing a set for coordinates that have been traversed
        traversed = set()
        BFSqueue = deque()


        # iterating through to find which numbers are 0's and adding coords of 0's to traversed (can consider 0's traversed because their distance from 0 is inherently 0)
        # (and adding to BFSqueue?????? maybe ?????)
        for i in range(maxRow):
            for j in range(maxCol):
                if mat[i][j] == 0:
                    traversed.add((i,j))
                    BFSqueue.append((i,j))

                   
            
        # do some kind of BFS shenanigans to update non-0's with if statements to check if neighbors are in bounds, and if they're not in the traversed set
        neighbors = [(0,-1), (0,1), (1,0), (-1,0)]   # north, south, east, west via adding the tuples to currCoords

        # continue looping until the queue is empty
        while len(BFSqueue) != 0:
            currCoords = BFSqueue.popleft()
            currRow, currCol = currCoords               # for readability

            # check neighboring boxes
            for i in neighbors:
                currNeighbor = (currRow + i[0],currCol+i[1])

                # if the neighbor isnt in traversed and is a valid box, distance of neighbor is distance of curr + 1
                if inBounds(currNeighbor) and currNeighbor not in traversed:
                    neiRow = currNeighbor[0]
                    neiCol = currNeighbor[1]

                    mat[neiRow][neiCol] = mat[currRow][currCol] + 1

                    traversed.add((neiRow, neiCol))
                    BFSqueue.append((neiRow, neiCol))

        return mat