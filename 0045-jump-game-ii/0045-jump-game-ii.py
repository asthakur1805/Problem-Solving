class Solution:

	def jump(self,nums):

		result = 0

		left, right = 0, 0

		while right < len(nums)-1:

			farthest = 0

			for index in range(left, right+1):

				farthest = max(farthest, index+nums[index])

			left, right, result = right+1, farthest, result+1

		return result