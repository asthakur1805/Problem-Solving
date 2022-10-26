class Solution:

	def searchMatrix(self, matrix, target):

		numRows, numColumns = len(matrix), len(matrix[0])

		leftPointer, rightPointer = 0, numRows * numColumns - 1

		while leftPointer <= rightPointer:

			midPointer = leftPointer + (rightPointer - leftPointer) // 2

			rowIndex, columnIndex = midPointer // numColumns, midPointer % numColumns

			if matrix[rowIndex][columnIndex] == target:

				return True

			if target < matrix[rowIndex][columnIndex]:

				rightPointer = midPointer - 1

			else:

				leftPointer = midPointer + 1

		return False