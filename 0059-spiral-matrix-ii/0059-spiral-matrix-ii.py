class Solution:

	def generateMatrix(self, matrixOrder):

		matrix = [[0] * matrixOrder for _ in range(matrixOrder)]

		leftPointer, rightPointer = 0, matrixOrder - 1  
	
		topPointer, bottomPointer = 0, matrixOrder - 1

		matrixElement = 1

		while leftPointer <= rightPointer:

			# Top Row

			for columnNumber in range(leftPointer, rightPointer+1):
				
				matrix[topPointer][columnNumber] = matrixElement
				matrixElement += 1

			topPointer += 1

			# Right Column

			for rowNumber in range(topPointer, bottomPointer+1):

				matrix[rowNumber][rightPointer] = matrixElement
				matrixElement+=1

			rightPointer -= 1

			# Bottom Row

			for columnNumber in range(rightPointer, leftPointer-1, -1):

				matrix[bottomPointer][columnNumber] = matrixElement
				matrixElement += 1

			bottomPointer -= 1

			# Left Column

			for rowNumber in range(bottomPointer, topPointer-1, -1):

				matrix[rowNumber][leftPointer] = matrixElement
				matrixElement += 1

			leftPointer += 1

		return matrix
	
		

		