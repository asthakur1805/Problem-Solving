from collections import deque

class Solution:

	def numEnclaves(self, grid):

		numRows, numColumns, visited, directions, totalLand, boundaryLand = len(grid), len(grid[0]), set({}), [(0,1),(0,-1),(1,0),(-1,0)], 0, 0

		queue = deque([])

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				totalLand += grid[currRow][currColumn]
	
				if grid[currRow][currColumn] == 1 and (currRow in (0,numRows-1) or currColumn in (0,numColumns-1)):

					boundaryLand += 1
					visited.add((currRow,currColumn))
					queue.append((currRow,currColumn))

		while queue:

			for _ in range(len(queue)):

				currRow, currColumn = queue.popleft()

				for rowDirection, columnDirection in directions:

					neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

					if 0<=neighborRow<numRows and 0<=neighborColumn<numColumns and (neighborRow,neighborColumn) not in visited and grid[neighborRow][neighborColumn]==1:

						visited.add((neighborRow,neighborColumn))
						queue.append((neighborRow,neighborColumn))
						boundaryLand += 1

		return totalLand-boundaryLand
			
					