class Solution:

	def sumSubarrayMins(self,nums):

		stack = []

		nextSmaller = [len(nums)]*len(nums)

		for currIndex in range(len(nums)):

			while stack and nums[currIndex] <= nums[stack[-1]]:

				nextSmaller[stack.pop()] = currIndex

			stack.append(currIndex)

		stack = []

		prevSmaller = [-1]*len(nums)
		
		for currIndex in range(len(nums)-1,-1,-1):

			while stack and nums[currIndex] < nums[stack[-1]]:

				prevSmaller[stack.pop()] = currIndex

			stack.append(currIndex)

		result = 0

		for currIndex in range(len(nums)):

			leftCandidates = currIndex - prevSmaller[currIndex] - 1

			rightCandidates = nextSmaller[currIndex] - currIndex - 1

			result = (result+(leftCandidates+1)*(rightCandidates+1)*nums[currIndex]) % (10**9+7)

		return result
