class Solution:

	def missingNumber(self, nums):

		existingNums = set(nums)

		for num in range(len(nums)+1):

			if num not in existingNums:

				return num