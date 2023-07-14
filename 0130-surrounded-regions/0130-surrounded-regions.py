from collections import deque

class Solution:

	def solve(self, board):

		numRows, numColumns, visited, queue, directions = len(board), len(board[0]), set({}), deque([]), [(0,1),(0,-1),(1,0),(-1,0)]

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if (currRow in (0,numRows-1) or currColumn in (0,numColumns-1)) and board[currRow][currColumn]=='O':

					visited.add((currRow,currColumn))
					queue.append((currRow,currColumn))

		while queue:

			for _ in range(len(queue)):

				currRow, currColumn = queue.popleft()

				for rowDirection, columnDirection in directions:

					neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

					if 0<=neighborRow<numRows and 0<=neighborColumn<numColumns and (neighborRow,neighborColumn) not in visited and board[neighborRow][neighborColumn]=='O':

						visited.add((neighborRow,neighborColumn))
						queue.append((neighborRow,neighborColumn))

		for currRow in range(1,numRows-1):

			for currColumn in range(1, numColumns-1):

				if board[currRow][currColumn] == 'O' and (currRow,currColumn) not in visited:

					board[currRow][currColumn] = 'X'

		return board

						

		