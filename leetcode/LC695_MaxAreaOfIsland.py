class Solution:      

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        traversed = set()
        self.maxIsland = 0                       # size of largest found island
        self.currIsland = 0                          # size of current island


        maxRow = len(grid)
        maxCol = len(grid[0])


        # helper function to determine if something is within boundaries
        def inBounds(coordsTuple):
            if (coordsTuple[0] < maxRow and coordsTuple[0] >= 0) and (coordsTuple[1] < maxCol and coordsTuple[1] >= 0):
                return True
            return False

        # helper function to flood fill (recursively) if a 1 is found
        def floodFill(row, col):
            self.currIsland += 1              # size of current island
            grid[row][col] += 1
            
            north = (row - 1, col)
            south = (row + 1, col)
            east = (row, col + 1)
            west = (row, col - 1)

            if (north not in traversed) and (inBounds(north)):
                if grid[north[0]][north[1]] == 1:
                    traversed.add(north)
                    floodFill(north[0], north[1])


            if (south not in traversed) and (inBounds(south)):
                if grid[south[0]][south[1]] == 1:
                    traversed.add(south)
                    floodFill(south[0], south[1])
                    1
            if (east not in traversed) and (inBounds(east)):
                if grid[east[0]][east[1]] == 1:
                    traversed.add(east)
                    floodFill(east[0], east[1])

            if (west not in traversed) and (inBounds(west)):
                if grid[west[0]][west[1]] == 1:
                    traversed.add(west)
                    floodFill(west[0], west[1])



        # iterate through array - O(n) where n is the total # of items in the entire grid
        for i in range(len(grid)):              
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.currIsland = 0
                    floodFill(i, j)
                    if self.currIsland > self.maxIsland:
                        self.maxIsland = self.currIsland

        return self.maxIsland
        