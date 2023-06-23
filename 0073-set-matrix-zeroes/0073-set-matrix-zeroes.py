class Solution:

	def setZeroes(self, matrix):

		numRows, numColumns = len(matrix), len(matrix[0])

		setRows, setColumns = [1]*numRows, [1]*numColumns

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if matrix[currRow][currColumn] == 0:

					setRows[currRow] = 0
					setColumns[currColumn] = 0

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if setRows[currRow] == 0 or setColumns[currColumn] == 0:
				
					matrix[currRow][currColumn] = 0