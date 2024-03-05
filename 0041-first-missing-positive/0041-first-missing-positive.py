class Solution:

	def firstMissingPositive(self,nums):

		numSet = set(nums)

		for num in range(1,len(nums)+2):

			if num not in numSet:

				return num

		