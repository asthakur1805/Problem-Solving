class Solution:

	def nextGreaterElements(self,nums):

		result = [-1] * len(nums)

		stack = []

		for currIndex in range(2*len(nums)):

			while stack and nums[currIndex%len(nums)] > nums[stack[-1]%len(nums)]:

				result[stack.pop()%len(nums)] = nums[currIndex%len(nums)]

			stack.append(currIndex)

		return result