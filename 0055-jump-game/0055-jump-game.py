class Solution:

	def canJump(self,nums):

		goal = len(nums)-1

		for index in range(len(nums)-2,-1,-1):

			if goal-index <= nums[index]:

				goal = index

		return goal == 0

		
		
		

		

		
		
		

		
		

		