class Solution:

	def canJump(self,nums):

		goal = len(nums)-1

		for currIndex in range(len(nums)-2,-1,-1):

			if currIndex+nums[currIndex] >= goal:

				goal = currIndex

		return goal == 0