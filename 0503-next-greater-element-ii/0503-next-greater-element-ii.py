class Solution:

	def nextGreaterElements(self,nums):

		result = [-1] * len(nums)

		for currIndex in range(len(nums)):

			for offset in range(1,len(nums)):

				nextIndex = (currIndex+offset) % len(nums)

				if nums[nextIndex] > nums[currIndex]:

					result[currIndex] = nums[nextIndex]
					break

		return result