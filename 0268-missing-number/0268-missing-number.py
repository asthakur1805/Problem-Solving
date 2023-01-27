class Solution:

	def missingNumber(self, nums):

		numsLength = len(nums)

		visitedNums = set()

		for num in nums:

			visitedNums.add(num)

		for num in range(numsLength+1):

			if num not in visitedNums:

				return num
