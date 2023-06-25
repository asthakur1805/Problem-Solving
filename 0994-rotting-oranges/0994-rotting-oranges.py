from collections import deque

class Solution:

	def orangesRotting(self, grid):

		# 0: Empty, 1: Fresh, 2: Rotten

		visited, numRows, numColumns, numFresh, queue = set(), len(grid), len(grid[0]), 0, deque([])

		for row in range(numRows):

			for column in range(numColumns):

				if grid[row][column] == 2:

					queue.append((row, column))
					visited.add((row, column))

				elif grid[row][column] == 1:

					numFresh += 1

		time, directions = 0, [(-1,0), (1,0), (0,-1), (0,1)]

		while queue and numFresh > 0:

			for _ in range(len(queue)):

				currRow, currColumn = queue.popleft()
				grid[currRow][currColumn] = 2

				for rowDirection, columnDirection in directions:

					neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

					if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and grid[neighborRow][neighborColumn] == 1 and (neighborRow, neighborColumn) not in visited:

						queue.append((neighborRow, neighborColumn))
						visited.add((neighborRow, neighborColumn))
						numFresh -= 1

			time += 1
	
		return time if not numFresh else -1 

		
				