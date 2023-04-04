class Solution:

	def searchMatrix(self, matrix, target):

		numRows, numColumns = len(matrix), len(matrix[0])

		for rowIndex in range(numRows):

			row = matrix[rowIndex]

			if self.binarySearch(row, target):

				return True

		return False

	def binarySearch(self, nums, target):

		left, right = 0, len(nums)-1

		while left <= right:

			mid = left + (right-left) // 2

			if nums[mid] == target:

				return True

			if nums[mid] < target:

				left = mid + 1

			else:

				right = mid - 1

		return False