class Solution:

	def floodFill(self,image,startRow,startColumn,newColor):

		numRows, numColumns, visited, directions, oldColor = len(image), len(image[0]), set(), [(-1,0),(1,0),(0,-1),(0,1)], image[startRow][startColumn]

		self.dfs(image,startRow,startColumn,numRows,numColumns,oldColor,newColor,directions,visited)

		return image

	def dfs(self,image,currRow,currColumn,numRows,numColumns,oldColor,newColor,directions,visited):

		visited.add((currRow,currColumn))
		image[currRow][currColumn] = newColor

		for rowDirection, columnDirection in directions:

			neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

			if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and (neighborRow,neighborColumn) not in visited and image[neighborRow][neighborColumn] == oldColor:

				self.dfs(image,neighborRow,neighborColumn,numRows,numColumns,oldColor,newColor,directions,visited)