class Solution:

	def pacificAtlantic(self,heights):

		numRows, numColumns, queuePacific, queueAtlantic, visitedPacific, visitedAtlantic = len(heights), len(heights[0]), deque([]), deque([]), set({}), set({})
		directions, result = [(-1,0),(1,0),(0,-1),(0,1)], []

		for currColumn in range(numColumns):

			queuePacific.append((0,currColumn))
			visitedPacific.add((0,currColumn))

			queueAtlantic.append((numRows-1,currColumn))
			visitedAtlantic.add((numRows-1,currColumn))

		for currRow in range(1,numRows):

			queuePacific.append((currRow,0))
			visitedPacific.add((currRow,0))

			queueAtlantic.append((currRow-1,numColumns-1))
			visitedAtlantic.add((currRow-1,numColumns-1))

		self.bfs(heights,queuePacific,visitedPacific,numRows,numColumns,directions)

		self.bfs(heights,queueAtlantic,visitedAtlantic,numRows,numColumns,directions)

		for (resultRow,resultColumn) in visitedPacific:

			if (resultRow,resultColumn) in visitedAtlantic:

				result.append([resultRow,resultColumn])

		return result

	def bfs(self,heights,queue,visited,numRows,numColumns,directions):

		while queue:

			currRow, currColumn = queue.popleft()

			for rowDirection,columnDirection in directions:

				neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

				if 0<=neighborRow<numRows and 0<=neighborColumn<numColumns and (neighborRow,neighborColumn) not in visited and heights[neighborRow][neighborColumn]>=heights[currRow][currColumn]:

					queue.append((neighborRow,neighborColumn))
					visited.add((neighborRow,neighborColumn))

	


	