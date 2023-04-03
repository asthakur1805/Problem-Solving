class Solution:

	def mySqrt(self, square):

		left, right = 1, square

		while left <= right:

			mid = left + (right - left) // 2

			if mid == square / mid:

				return mid

			if mid < square / mid:

				left = mid + 1

			else:

				right = mid - 1

		return right