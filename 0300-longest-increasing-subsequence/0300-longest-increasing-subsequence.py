class Solution:

	def lengthOfLIS(self,nums):

		subSequence = []

		for num in nums:

			if len(subSequence) == 0 or subSequence[-1] < num:

				subSequence.append(num)

			else:

				insertIndex = self.searchInsert(subSequence,num)

				subSequence[insertIndex] = num

		return len(subSequence)

	def searchInsert(self,nums,target):

		left, right = 0, len(nums)-1

		while left <= right:

			mid = left + (right - left) // 2

			if nums[mid] == target:

				return mid

			if target < nums[mid]:

				right = mid - 1

			else:

				left = mid + 1

		return left