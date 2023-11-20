class Solution:

	def pacificAtlantic(self,heights):

		numRows, numColumns, visitedPacific, visitedAtlantic, directions, result = len(heights), len(heights[0]), set(), set(), [(-1,0),(1,0),(0,-1),(0,1)], []

		for currColumn in range(numColumns):

			self.dfs(heights,0,currColumn,numRows,numColumns,visitedPacific,directions)
			self.dfs(heights,numRows-1,currColumn,numRows,numColumns,visitedAtlantic,directions)

		for currRow in range(1,numRows):

			self.dfs(heights,currRow,0,numRows,numColumns,visitedPacific,directions)
			self.dfs(heights,currRow-1,numColumns-1,numRows,numColumns,visitedAtlantic,directions)

		for (resultRow,resultColumn) in visitedPacific:

			if (resultRow,resultColumn) in visitedAtlantic:

				result.append([resultRow,resultColumn])

		return result

	def dfs(self,heights,currRow,currColumn,numRows,numColumns,visited,directions):

		visited.add((currRow,currColumn))

		for rowDirection,columnDirection in directions:

			neighborRow, neighborColumn = currRow+rowDirection,currColumn+columnDirection

			if 0<=neighborRow<numRows and 0<=neighborColumn<numColumns and (neighborRow,neighborColumn) not in visited and heights[neighborRow][neighborColumn]>=heights[currRow][currColumn]:

				self.dfs(heights,neighborRow,neighborColumn,numRows,numColumns,visited,directions)

	


			