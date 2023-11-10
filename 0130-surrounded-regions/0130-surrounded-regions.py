from collections import deque

class Solution:

	def solve(self,board):

		numRows, numColumns, visited, directions = len(board), len(board[0]), set({}), [(-1,0),(1,0),(0,-1),(0,1)]

		queue = deque([])

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if board[currRow][currColumn] == "O" and (currRow in (0,numRows-1) or currColumn in (0,numColumns-1)):

					queue.append((currRow,currColumn))
					visited.add((currRow,currColumn))

		while queue:

			currRow,currColumn = queue.popleft()

			for rowDirection,columnDirection in directions:

				neighborRow,neighborColumn = currRow+rowDirection, currColumn+columnDirection

				if 0<=neighborRow<numRows and 0<=neighborColumn<numColumns and (neighborRow,neighborColumn) not in visited and board[neighborRow][neighborColumn] == 'O':

					queue.append((neighborRow,neighborColumn))
					visited.add((neighborRow,neighborColumn))

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if (currRow,currColumn) not in visited:

					board[currRow][currColumn] = 'X'

			