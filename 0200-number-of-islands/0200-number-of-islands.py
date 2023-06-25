class Solution:

	def numIslands(self, grid):

		numRows, numColumns, visited, count = len(grid), len(grid[0]), set({}), 0

		for row in range(numRows):

			for column in range(numColumns):

				if grid[row][column] == "1" and (row, column) not in visited:
					
					count += 1
					self.dfs(grid, row, column, numRows, numColumns, visited)

		return count

	def dfs(self, grid, row, column, numRows, numColumns, visited):

		visited.add((row,column))

		searchDirections = [(-1,0), (1,0), (0,1), (0,-1)]

		for rowDirection, columnDirection in searchDirections:

			neighborRow, neighborColumn = row+rowDirection, column+columnDirection
 
			if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and grid[neighborRow][neighborColumn] == "1" and (neighborRow, neighborColumn) not in visited:

				self.dfs(grid, neighborRow, neighborColumn, numRows, numColumns, visited)
