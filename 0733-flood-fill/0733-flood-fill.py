from collections import deque

class Solution:

	def floodFill(self, image, startRow, startColumn, newColor):

		numRows, numColumns = len(image), len(image[0])

		self.bfs(image, startRow, startColumn, numRows, numColumns, newColor)

		return image

	def bfs(self, image, startRow, startColumn, numRows, numColumns, newColor):

		oldColor = image[startRow][startColumn]
		visited = set({(startRow,startColumn)})
		queue = deque([(startRow,startColumn)])
		directions = [(-1,0), (1,0), (0,-1), (0,1)]

		while queue:

			for _ in range(len(queue)):
	
				currRow, currColumn = queue.popleft()
				image[currRow][currColumn] = newColor

				for rowDirection, columnDirection in directions:

					neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

					if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and image[neighborRow][neighborColumn] == oldColor and (neighborRow,neighborColumn) not in visited:

						queue.append((neighborRow, neighborColumn))
						visited.add((neighborRow, neighborColumn))
	
				
				

		
