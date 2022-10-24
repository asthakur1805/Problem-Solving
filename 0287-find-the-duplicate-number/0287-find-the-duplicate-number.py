class Solution:

	def findDuplicate(self, nums):

		visitedNums = set()

		for num in nums:

			if num in visitedNums:

				return num

			visitedNums.add(num)


		