class Solution:

	def jump(self,nums):

		left, right, result = 0, 0, 0

		while right < len(nums)-1:

			farthest = right

			for index in range(left,right+1):

				farthest = max(farthest,index+nums[index])

			left, right, result = right+1, farthest, result+1

		return result