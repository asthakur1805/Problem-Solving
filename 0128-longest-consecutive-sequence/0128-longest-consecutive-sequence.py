class Solution:

	def longestConsecutive(self, nums):

		numSet, resultLength = set(nums), 0

		for num in numSet:

			if num-1 not in numSet:

				currLength = 1

				while num + currLength in numSet:

					currLength += 1

				resultLength = max(resultLength, currLength)

		return resultLength