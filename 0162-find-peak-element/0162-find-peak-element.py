class Solution:

	def findPeakElement(self, nums):

		left, right = 0, len(nums)-1

		while left <= right:

			mid = left + (right - left) // 2

			if left == right or nums[mid-1] < nums[mid] > nums[mid+1]:

				return mid

			if nums[mid+1] > nums[mid]:

				left = mid + 1

			else:

				right = mid - 1