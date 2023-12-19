class Solution:

	def minPathSum(self,grid):

		numRows, numColumns = len(grid), len(grid[0])

		prev = [0]*numColumns

		for currRow in range(numRows-1,-1,-1):

			curr = [0]*numColumns 

			for currColumn in range(numColumns-1,-1,-1):

				if (currRow,currColumn) == (numRows-1,numColumns-1):

					curr[currColumn] = grid[currRow][currColumn]

				else:
					
					right = curr[currColumn+1] if currColumn < numColumns-1 else float('inf')
					down = prev[currColumn] if currRow < numRows-1 else float('inf')

					curr[currColumn] = grid[currRow][currColumn] + min(right,down)
			
			prev = curr

		return prev[0]

					

					
