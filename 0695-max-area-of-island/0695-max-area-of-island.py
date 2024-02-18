from collections import deque

class Solution:

	def maxAreaOfIsland(self,grid):

		numRows, numColumns = len(grid), len(grid[0])

		visited, directions = set(), [(-1,0),(1,0),(0,-1),(0,1)]

		self.result = 0

		for startRow in range(numRows):

			for startColumn in range(numColumns):

				if grid[startRow][startColumn] == 1 and (startRow,startColumn) not in visited:

					self.bfs(grid,startRow,startColumn,numRows,numColumns,visited,directions)

		return self.result

	def bfs(self,grid,startRow,startColumn,numRows,numColumns,visited,directions):

		queue = deque([(startRow,startColumn)])
		visited.add((startRow,startColumn))
		currIslandArea = 0

		while queue:

			currRow,currColumn = queue.popleft()
			currIslandArea += 1

			for rowDirection, columnDirection in directions:

				neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

				if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and grid[neighborRow][neighborColumn] == 1 and (neighborRow,neighborColumn) not in visited:

					queue.append((neighborRow,neighborColumn))
					visited.add((neighborRow,neighborColumn))

		self.result = max(self.result,currIslandArea)
			
		