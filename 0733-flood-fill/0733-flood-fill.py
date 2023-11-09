from collections import deque

class Solution:

	def floodFill(self,image,startRow,startColumn,newColor):

		oldColor, numRows, numColumns, visited, directions = image[startRow][startColumn], len(image), len(image[0]), set({}), [(-1,0),(1,0),(0,-1),(0,1)]

		queue = deque([(startRow,startColumn)])
		visited.add((startRow,startColumn))

		while queue:

			currRow, currColumn = queue.popleft()

			image[currRow][currColumn] = newColor

			for rowDirection, columnDirection in directions:

				neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

				if 0<=neighborRow<numRows and 0<=neighborColumn<numColumns and image[neighborRow][neighborColumn] == oldColor and (neighborRow,neighborColumn) not in visited:

					queue.append((neighborRow,neighborColumn))
					visited.add((neighborRow,neighborColumn))

		return image
		