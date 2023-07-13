class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        starting from the bottom, work your way up the triangle, updating parents with the smallest 
        sum of the children subtrees, and return first item
        '''
        def kindaDFS(vertCoord):
            # base case: top of the triangle
            if vertCoord == 0:
                return

            # updates parent
            for i in range(len(triangle[vertCoord])-1):
                triangle[vertCoord-1][i] = triangle[vertCoord-1][i] + min(triangle[vertCoord][i], triangle[vertCoord][i+1])

            # recurse
            kindaDFS(vertCoord-1)
            
        kindaDFS(len(triangle)-1)

        return triangle[0][0]


        '''
        try this starting from the top
        '''