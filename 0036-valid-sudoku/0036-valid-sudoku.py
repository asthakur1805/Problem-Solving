class Solution:

	def isValidSudoku(self, board):

		rowSets = [set() for _ in range(9)]
		columnSets = [set() for _ in range(9)]
		boxSets = [set() for _ in range(9)]

		for rowNumber in range(9):

			for columnNumber in range(9):

				boardValue = board[rowNumber][columnNumber]

				if boardValue != '.':

					boxNumber = (rowNumber // 3) * 3 + (columnNumber // 3)

					if boardValue in rowSets[rowNumber] or boardValue in columnSets[columnNumber] or boardValue in boxSets[boxNumber]:
						
						return False

					rowSets[rowNumber].add(boardValue)
					columnSets[columnNumber].add(boardValue)
					boxSets[boxNumber].add(boardValue)

		return True
		