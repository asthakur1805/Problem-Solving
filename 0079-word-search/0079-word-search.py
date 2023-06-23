class Solution:

	def exist(self, grid, word):

		numRows, numColumns, visited = len(grid), len(grid[0]), set()

		for row in range(numRows):

			for column in range(numColumns):

				if self.dfs(grid,  word, 0, row, column, numRows, numColumns, visited):

					return True

		return False

	def dfs(self, grid, word, index, row, column, numRows, numColumns, visited):

		if index == len(word):

			return True

		if row < 0 or row == numRows or column < 0 or column == numColumns or grid[row][column] != word[index] or (row, column) in visited:

			return False

		visited.add((row, column))
		
		result = (self.dfs(grid, word, index+1, row, column-1, numRows, numColumns, visited) or
				  self.dfs(grid, word, index+1, row, column+1, numRows, numColumns, visited) or
				  self.dfs(grid, word, index+1, row-1, column, numRows, numColumns, visited) or
				  self.dfs(grid, word, index+1, row+1, column, numRows, numColumns, visited))

		visited.remove((row, column))

		return result