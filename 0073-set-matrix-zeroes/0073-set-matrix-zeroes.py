class Solution:

	def setZeroes(self, matrix):

		numRows, numColumns = len(matrix), len(matrix[0])

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if matrix[currRow][currColumn] == 0:

					for zeroRow in range(numRows):

						if matrix[zeroRow][currColumn] != 0:

							matrix[zeroRow][currColumn] = None

					for zeroColumn in range(numColumns):

						if matrix[currRow][zeroColumn] != 0:

							matrix[currRow][zeroColumn] = None

		for currRow in range(numRows):

			for currColumn in range(numColumns):

				if matrix[currRow][currColumn] == None:

					matrix[currRow][currColumn] = 0

						

						