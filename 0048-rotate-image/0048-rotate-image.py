class Solution:

	def rotate(self, matrix):

		leftPointer, rightPointer = 0, len(matrix)-1

		while leftPointer < rightPointer:

			topPointer, bottomPointer = leftPointer, rightPointer

			for offset in range(rightPointer - leftPointer):

				topLeft = matrix[topPointer][leftPointer+offset]

				matrix[topPointer][leftPointer+offset] = matrix[bottomPointer-offset][leftPointer]

				matrix[bottomPointer-offset][leftPointer] = matrix[bottomPointer][rightPointer-offset]

				matrix[bottomPointer][rightPointer-offset] = matrix[topPointer+offset][rightPointer]

				matrix[topPointer+offset][rightPointer] = topLeft

			leftPointer += 1
			rightPointer -= 1

		
