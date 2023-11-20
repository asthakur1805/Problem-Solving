from collections import deque

class Solution:

	def pacificAtlantic(self,heights):

		numRows, numColumns, directions, resultSet = len(heights), len(heights[0]), [(-1,0),(1,0),(0,-1),(0,1)], set({})

		for startRow in range(numRows):

			for startColumn in range(numColumns):

				self.visitedPacific = self.visitedAtlantic = False

				self.bfs(heights,startRow,startColumn,numRows,numColumns,directions,resultSet)

		result = []

		for (resultRow,resultColumn) in resultSet:

			result.append([resultRow,resultColumn])

		return result

	def bfs(self,heights,startRow,startColumn,numRows,numColumns,directions,resultSet):

		queue, visited = deque([(startRow,startColumn)]), set({(startRow,startColumn)})

		while queue:

			currRow,currColumn = queue.popleft()

			for rowDirection, columnDirection in directions:

				neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

				if neighborRow == -1 or neighborColumn == -1:

					self.visitedPacific = True

				if neighborRow == numRows or neighborColumn == numColumns:

					self.visitedAtlantic = True

				if self.visitedPacific and self.visitedAtlantic:

					resultSet.add((startRow,startColumn))

				if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and (neighborRow,neighborColumn) not in visited and heights[neighborRow][neighborColumn] <= heights[currRow][currColumn]:

					queue.append((neighborRow,neighborColumn))

					visited.add((neighborRow,neighborColumn))

