class Solution:

	def missingNumber(self, nums):

		visitedNums = set()

		for num in nums:

			visitedNums.add(num)

		for num in range(len(nums)+1):

			if num not in visitedNums:

				return num

		