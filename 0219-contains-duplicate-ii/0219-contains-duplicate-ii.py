class Solution:

	def containsNearbyDuplicate(self, nums, indexDiff):

		numSet = set()

		for index, num in enumerate(nums):

			if num in numSet:

				return True

			numSet.add(num)

			if len(numSet) > indexDiff:

				numSet.remove(nums[index-indexDiff])

		return False