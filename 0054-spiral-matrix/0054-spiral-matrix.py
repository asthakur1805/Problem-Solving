class Solution:

	def spiralOrder(self, matrix):

		numRows, numColumns = len(matrix), len(matrix[0])

		result = []

		leftPointer, rightPointer = 0, numColumns-1
		
		topPointer, bottomPointer = 0, numRows-1

		while leftPointer <= rightPointer and topPointer <= bottomPointer:

			for columnNumber in range(leftPointer, rightPointer+1):

				result.append(matrix[topPointer][columnNumber])

			topPointer += 1

			for rowNumber in range(topPointer, bottomPointer+1):

				result.append(matrix[rowNumber][rightPointer])

			rightPointer -= 1
			
			
			if topPointer <= bottomPointer:
			
				for columnNumber in range(rightPointer, leftPointer-1, -1):

					result.append(matrix[bottomPointer][columnNumber])

				bottomPointer -= 1

			if leftPointer <= rightPointer:

				for rowNumber in range(bottomPointer, topPointer-1, -1):

					result.append(matrix[rowNumber][leftPointer])

				leftPointer += 1

		return result
		