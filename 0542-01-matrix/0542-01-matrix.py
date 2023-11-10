from collections import deque

class Solution:

	def updateMatrix(self,matrix):

		numRows, numColumns, visited, directions = len(matrix), len(matrix[0]), set({}), [(-1,0),(1,0),(0,-1),(0,1)]

		queue = deque([])

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if matrix[currRow][currColumn] == 0:
				
					queue.append((currRow,currColumn))
					visited.add((currRow,currColumn))

		while queue:
	
			currRow,currColumn = queue.popleft()

			for rowDirection,columnDirection in directions:

				neighborRow,neighborColumn = currRow+rowDirection, currColumn+columnDirection

				if 0<=neighborRow<numRows and 0<=neighborColumn<numColumns and matrix[neighborRow][neighborColumn]==1 and (neighborRow,neighborColumn) not in visited:

					matrix[neighborRow][neighborColumn]=matrix[currRow][currColumn]+1
					queue.append((neighborRow,neighborColumn))
					visited.add((neighborRow,neighborColumn))

		return matrix