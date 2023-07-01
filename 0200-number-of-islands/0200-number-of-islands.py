class Solution:

	def numIslands(self, grid):

		numberRows, numberColumns, count, visited, directions = len(grid), len(grid[0]), 0, set(), [(0,1),(1,0),(0,-1),(-1,0)]

		for currRow in range(numberRows):

			for currColumn in range(numberColumns):

				if grid[currRow][currColumn] == "1" and (currRow,currColumn) not in visited:

					count += 1
					self.dfs(grid, currRow, currColumn, numberRows, numberColumns, visited, directions)

		return count

	def dfs(self, grid, currRow, currColumn, numberRows, numberColumns, visited, directions):

		visited.add((currRow, currColumn))

		for rowDirection, columnDirection in directions:

			neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

			if 0 <= neighborRow < numberRows and 0 <= neighborColumn < numberColumns and (neighborRow,neighborColumn) not in visited and grid[neighborRow][neighborColumn] == "1":

				self.dfs(grid, neighborRow, neighborColumn, numberRows, numberColumns, visited, directions)