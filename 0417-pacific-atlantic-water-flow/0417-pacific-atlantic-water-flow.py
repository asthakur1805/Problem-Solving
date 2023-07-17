from collections import deque

class Solution:

	def pacificAtlantic(self, heights):

		numRows, numColumns, visitedPacific, visitedAtlantic, directions = len(heights), len(heights[0]), set(), set(), [(0,1),(0,-1),(1,0),(-1,0)]

		queuePacific, queueAtlantic = deque([]),deque([])

		for column in range(numColumns):

			queuePacific.append((0,column))
			queueAtlantic.append((numRows-1,column))

		for row in range(1, numRows):

			queuePacific.append((row,0))
			queueAtlantic.append((row-1,numColumns-1))

		self.bfs(heights,queuePacific,visitedPacific,numRows,numColumns,directions)
		self.bfs(heights,queueAtlantic,visitedAtlantic,numRows,numColumns,directions)

		result = []

		for (row,column) in visitedPacific: 

			if (row,column) in visitedAtlantic:

				result.append([row,column])

		return result

	def bfs(self,heights,queue,visited,numRows,numColumns,directions):


		while queue:

			currRow, currColumn = queue.popleft()
			visited.add((currRow,currColumn))
			
			for rowDirection, columnDirection in directions:

				neighborRow,neighborColumn = currRow+rowDirection,currColumn+columnDirection

				if 0<=neighborRow<numRows and 0<=neighborColumn<numColumns and (neighborRow,neighborColumn) not in visited and heights[currRow][currColumn]<=heights[neighborRow][neighborColumn]:
		
					queue.append((neighborRow,neighborColumn))
			
		

			