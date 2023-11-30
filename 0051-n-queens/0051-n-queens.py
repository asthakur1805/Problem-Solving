class Solution:

	def solveNQueens(self,N):

		colSet, posDiagSet, negDiagSet = set(), set(), set()

		board = [['.' for _ in range(N)] for _ in range(N)]

		result = []

		self.helper(board,0,N,colSet,posDiagSet,negDiagSet,result)

		return result

	def helper(self,board,row,N,colSet,posDiagSet,negDiagSet,result):

		if row == N:

			boardCopy = [''.join(row) for row in board]

			result.append(boardCopy)

			return

		for column in range(N):

			if column in colSet or row+column in posDiagSet or row-column in negDiagSet:

				continue

			colSet.add(column)
			posDiagSet.add(row+column)
			negDiagSet.add(row-column)
			board[row][column]='Q'

			self.helper(board,row+1,N,colSet,posDiagSet,negDiagSet,result)

			colSet.remove(column)
			posDiagSet.remove(row+column)
			negDiagSet.remove(row-column)
			board[row][column]='.'

			