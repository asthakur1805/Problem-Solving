class Solution:

	def rotate(self, matrix):

		topPointer, bottomPointer = 0, len(matrix)-1

		while topPointer < bottomPointer:

			matrix[topPointer], matrix[bottomPointer] = matrix[bottomPointer], matrix[topPointer]
			topPointer += 1
			bottomPointer -= 1

		for rowNumber in range(len(matrix)):

			for columnNumber in range(rowNumber+1, len(matrix)):

				matrix[rowNumber][columnNumber], matrix[columnNumber][rowNumber] = matrix[columnNumber][rowNumber], matrix[rowNumber][columnNumber]
		
		
