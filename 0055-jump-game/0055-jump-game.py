class Solution:

	def canJump(self,nums):

		goal = len(nums)-1

		for index in range(len(nums)-2,-1,-1):

			if index + nums[index] >= goal:

				goal = index

		return goal == 0