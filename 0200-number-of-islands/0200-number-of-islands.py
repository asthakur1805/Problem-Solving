from collections import deque

class Solution:

	def numIslands(self, grid):

		numRows, numColumns, visited, count = len(grid), len(grid[0]), set({}), 0

		for row in range(numRows):

			for column in range(numColumns):

				if grid[row][column] == "1" and (row, column) not in visited:
					
					count += 1
					self.bfs(grid, row, column, numRows, numColumns, visited)

		return count

	def bfs(self, grid, row, column, numRows, numColumns, visited):

		visited.add((row, column))
		queue = deque([(row, column)])

		searchDirections = [(-1,0), (1,0), (0,-1), (0,1)]

		while queue:

			for _ in range(len(queue)):

				currRow, currColumn = queue.popleft()

				for rowDelta, columnDelta in searchDirections:

					neighborRow, neighborColumn = currRow+rowDelta, currColumn+columnDelta

					if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and grid[neighborRow][neighborColumn] == "1" and (neighborRow, neighborColumn) not in visited:

						visited.add((neighborRow, neighborColumn))
						queue.append((neighborRow, neighborColumn))

	