class Solution:

	def jump(self,nums):

		return self.helper(nums,0,{})

	def helper(self,nums,index,cache):

		if index == len(nums)-1: return 0

		if index in cache:

			return cache[index]

		minJumps = float('inf')

		for jump in range(1,nums[index]+1):

			if index+jump < len(nums):

				minJumps = min(minJumps,1+self.helper(nums,index+jump,cache))

		cache[index] = minJumps

		return minJumps