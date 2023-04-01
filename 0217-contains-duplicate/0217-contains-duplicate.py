class Solution:

	def containsDuplicate(self, nums):

		visitedNums = set()

		for num in nums:

			if num in visitedNums:

				return True

			visitedNums.add(num)

		return False