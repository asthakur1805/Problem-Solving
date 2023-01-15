class Solution:

	def singleNumber(self, nums):

		visitedNums = set()

		for num in nums:

			if num in visitedNums:

				visitedNums.remove(num)

			else:

				visitedNums.add(num)

		for num in visitedNums:

			return num