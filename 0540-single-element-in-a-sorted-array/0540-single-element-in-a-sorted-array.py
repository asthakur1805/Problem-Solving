class Solution:

	def singleNonDuplicate(self,nums):

		left, right = 0, len(nums)-1

		while left <= right:

			mid = left + (right - left) // 2

			prevElement = nums[mid-1] if mid >= 1 else float('-inf')
			nextElement = nums[mid+1] if mid < len(nums)-1 else float('inf')

			if prevElement < nums[mid] < nextElement:

				return nums[mid]

			leftPartitionSize = (mid-2)-left+1 if nums[mid] == prevElement else (mid-1)-left+1

			if leftPartitionSize % 2:

				right = mid - (2 if nums[mid] == prevElement else 1)
 
			else:

				left = mid + (2 if nums[mid] == nextElement else 1)

		