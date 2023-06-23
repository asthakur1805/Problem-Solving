class Solution:

	def setZeroes(self, matrix):

		numRows, numColumns, firstColumn = len(matrix), len(matrix[0]), 1

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if matrix[currRow][currColumn] == 0:

					matrix[currRow][0] = 0

					if currColumn > 0:

						matrix[0][currColumn] = 0

					else:

						firstColumn = 0

		for currRow in range(1, numRows):

			for currColumn in range(1, numColumns):

				if matrix[0][currColumn] == 0 or matrix[currRow][0] == 0:

					matrix[currRow][currColumn] = 0

		if matrix[0][0] == 0:
		
			for currColumn in range(1, numColumns):

				matrix[0][currColumn] = 0

		if firstColumn == 0:

			for currRow in range(numRows):

				matrix[currRow][0] = 0

			

		