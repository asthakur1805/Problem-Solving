class Solution:

	def jump(self,nums):

		return self.helper(nums,0,{})

	def helper(self,nums,index,cache):

		if index == len(nums)-1:

			return 0

		result = float('inf')

		if index in cache:

			return cache[index]

		for jumpSize in range(1,nums[index]+1):

			if index+jumpSize < len(nums):

				result = min(result,1+self.helper(nums,index+jumpSize,cache))

		cache[index] = result
		return result