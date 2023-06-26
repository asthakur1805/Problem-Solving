from collections import deque

class Solution:

	def updateMatrix(self, matrix):

		numberRows, numberColumns, queue, visited, directions = len(matrix), len(matrix[0]), deque([]), set(), [(-1,0),(1,0),(0,-1),(0,1)]

		for row in range(numberRows):

			for column in range(numberColumns):

				if matrix[row][column] == 0:

					visited.add((row,column))
					queue.append((row,column))

		while queue:

			for _ in range(len(queue)):

				currRow, currColumn = queue.popleft()

				for rowDirection, columnDirection in directions:

					neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

					if 0 <= neighborRow < numberRows and 0 <= neighborColumn < numberColumns and (neighborRow, neighborColumn) not in visited:

						matrix[neighborRow][neighborColumn] = matrix[currRow][currColumn]+1

						visited.add((neighborRow, neighborColumn))

						queue.append((neighborRow, neighborColumn))

		return matrix