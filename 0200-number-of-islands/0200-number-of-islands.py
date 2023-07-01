from collections import deque

class Solution:

	def numIslands(self, grid):

		numRows, numColumns, count, visited, directions = len(grid), len(grid[0]), 0, set(), [(0,1),(0,-1),(1,0),(-1,0)]

		for startRow in range(numRows):

			for startColumn in range(numColumns):

				if grid[startRow][startColumn] == '1' and (startRow, startColumn) not in visited:

					count += 1
					self.bfs(grid, startRow, startColumn, numRows, numColumns, visited, directions)

		return count

	def bfs(self, grid, startRow, startColumn, numRows, numColumns, visited, directions):

		visited.add((startRow,startColumn))
		queue = deque([(startRow,startColumn)])

		while queue:

			for _ in range(len(queue)):

				currRow, currColumn = queue.popleft()

				for rowDirection, columnDirection in directions:

					neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection
				
					if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and grid[neighborRow][neighborColumn] == '1' and (neighborRow,neighborColumn) not in visited:

						visited.add((neighborRow,neighborColumn))
						queue.append((neighborRow,neighborColumn))

			