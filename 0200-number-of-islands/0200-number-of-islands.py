from collections import deque

class Solution:

	def numIslands(self,grid):

		result, visited, numRows, numColumns, directions = 0, set(), len(grid), len(grid[0]), [(-1,0),(1,0),(0,-1),(0,1)]

		for startRow in range(numRows):

			for startColumn in range(numColumns):

				if grid[startRow][startColumn] == "1" and (startRow,startColumn) not in visited:

					result += 1
					self.bfs(grid,startRow,startColumn,numRows,numColumns,visited,directions)

		return result

	def bfs(self,grid,startRow,startColumn,numRows,numColumns,visited,directions):

		queue = deque([(startRow,startColumn)])
		visited.add((startRow,startColumn))

		while queue:

			currRow, currColumn = queue.popleft()

			for rowDirection, columnDirection in directions:

				neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

				if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and grid[neighborRow][neighborColumn] == "1" and (neighborRow,neighborColumn) not in visited:

					queue.append((neighborRow,neighborColumn))
					visited.add((neighborRow,neighborColumn))

					