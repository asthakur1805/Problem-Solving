class Solution:

	def setZeroes(self, matrix):

		numRows, numColumns = len(matrix), len(matrix[0])

		setRows, setColumns = [False]*numRows, [False]*numColumns

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if matrix[currRow][currColumn] == 0:

					setRows[currRow], setColumns[currColumn] = True, True

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if setRows[currRow] or setColumns[currColumn]:

					matrix[currRow][currColumn] = 0

	