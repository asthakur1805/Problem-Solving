class Solution:

	def jump(self,nums):

		return self.helper(nums,0,{})

	def helper(self,nums,index,cache):

		if index == len(nums)-1:

			return 0

		if index in cache:

			return cache[index]

		cache[index] = float('inf')

		for jump in range(1,nums[index]+1):

			if index + jump < len(nums):

				cache[index] = min(cache[index],1+self.helper(nums,index+jump,cache))

		return cache[index]

		
		