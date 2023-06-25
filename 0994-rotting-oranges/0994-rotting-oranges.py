from collections import deque

class Solution:

	def orangesRotting(self, grid):

		# 0: Empty, 1: Fresh, 2: Rotten

		numRows, numColumns, numFresh, directions, queue = len(grid), len(grid[0]), 0, [(-1,0), (1,0), (0,-1), (0,1)], deque([])

		for row in range(numRows):

			for column in range(numColumns):

				if grid[row][column] == 2:

					queue.append((row, column))

				elif grid[row][column] == 1:

					numFresh += 1

		time = 0

		while queue and numFresh > 0:

			for _ in range(len(queue)):

				currRow, currColumn = queue.popleft()

				for rowDirection, columnDirection in directions:

					neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

					if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and grid[neighborRow][neighborColumn] == 1:

						numFresh -= 1
						queue.append((neighborRow, neighborColumn))
						grid[neighborRow][neighborColumn] = 2

			time += 1

		return time if numFresh == 0 else -1

		

			

		

		