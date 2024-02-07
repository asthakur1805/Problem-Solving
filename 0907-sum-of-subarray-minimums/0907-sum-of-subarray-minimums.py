class Solution:

	def sumSubarrayMins(self,nums):

		stack = []

		result = 0

		for	currIndex in range(len(nums)+1):

			while stack and (currIndex == len(nums) or nums[currIndex] < nums[stack[-1]]):

				nextSmaller = currIndex
				prevSmaller = stack[-2] if len(stack) > 1 else -1

				prevIndex = stack.pop()

				leftCandidates = (prevIndex-prevSmaller-1)	
				rightCandidates = (nextSmaller-prevIndex-1)

				result = (result + (leftCandidates+1)*(rightCandidates+1)*nums[prevIndex]) % (10**9+7)

			stack.append(currIndex)

		return result

				

				