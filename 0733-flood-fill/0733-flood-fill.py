from collections import deque

class Solution:

	def floodFill(self,image,startRow,startColumn,newColor):

		numRows, numColumns, directions, oldColor = len(image), len(image[0]), [(-1,0),(1,0),(0,-1),(0,1)], image[startRow][startColumn]

		queue = deque([(startRow,startColumn)])
		visited = set({(startRow,startColumn)})

		while queue:

			currRow, currColumn = queue.popleft()

			image[currRow][currColumn] = newColor

			for rowDirection, columnDirection in directions:

				neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

				if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and (neighborRow,neighborColumn) not in visited and image[neighborRow][neighborColumn] == oldColor:

					queue.append((neighborRow,neighborColumn))
					visited.add((neighborRow,neighborColumn))

		return image

				

			

			