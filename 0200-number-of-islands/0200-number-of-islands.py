class Solution:

	def numIslands(self,grid):

		numRows, numColumns, visited, directions, result = len(grid), len(grid[0]), set(), [(-1,0),(1,0),(0,-1),(0,1)], 0

		for startRow in range(numRows):

			for startColumn in range(numColumns):

				if grid[startRow][startColumn] == "1" and (startRow,startColumn) not in visited:

					result += 1
					
					self.dfs(grid,startRow,startColumn,numRows,numColumns,visited,directions)

		return result

	def dfs(self,grid,currRow,currColumn,numRows,numColumns,visited,directions):

		visited.add((currRow,currColumn))

		for rowDirection, columnDirection in directions:

			neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

			if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and grid[neighborRow][neighborColumn] == "1" and (neighborRow,neighborColumn) not in visited:

				self.dfs(grid,neighborRow,neighborColumn,numRows,numColumns,visited,directions)

					