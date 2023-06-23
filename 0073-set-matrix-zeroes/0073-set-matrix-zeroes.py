class Solution:

	def setZeroes(self, matrix):

		numRows, numColumns = len(matrix), len(matrix[0])

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if matrix[currRow][currColumn] == 0:

					for row in range(numRows):

						if matrix[row][currColumn] != 0:

							matrix[row][currColumn] = None

					for column in range(numColumns):

						if matrix[currRow][column] != 0:

							matrix[currRow][column] = None

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if matrix[currRow][currColumn] == None:

					matrix[currRow][currColumn] = 0

