from collections import deque

class Solution:

	def solve(self, board):

		numRows, numColumns, visited, queue, directions = len(board), len(board[0]), set(), deque([]), [(-1,0),(1,0),(0,-1),(0,1)]

		for column in range(numColumns):

			if board[0][column] == 'O' and board[0][column] not in visited:

				visited.add((0,column))
				queue.append((0,column))

			if board[numRows-1][column] == 'O' and board[numRows-1][column] not in visited:

				visited.add((numRows-1,column))
				queue.append((numRows-1,column))

		for row in range(1,numRows-1):

			if board[row][0] == 'O' and board[row][0] not in visited:

				visited.add((row,0))
				queue.append((row,0))

			if board[row][numColumns-1] == 'O' and board[row][numColumns-1] not in visited:

				visited.add((row,numColumns-1))
				queue.append((row,numColumns-1))

		while queue:

			for _ in range(len(queue)):

				currRow, currColumn = queue.popleft()

				for rowDirection, columnDirection in directions:

					neighborRow, neighborColumn = currRow+rowDirection, currColumn+columnDirection

					if 0 <= neighborRow < numRows and 0 <= neighborColumn < numColumns and board[neighborRow][neighborColumn]=='O' and (neighborRow, neighborColumn) not in visited:

						visited.add((neighborRow,neighborColumn))
						queue.append((neighborRow, neighborColumn))

		for row in range(numRows):

			for column in range(numColumns):

				if board[row][column] == 'O' and (row,column) not in visited:

					board[row][column] = 'X'
		