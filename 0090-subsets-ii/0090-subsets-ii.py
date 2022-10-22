class Solution:

	def subsetsWithDup(self, nums):

		nums.sort()

		index = 0

		currSubset = []

		result = []

		self.helper(nums, index, currSubset, result)

		return result

	def helper(self, nums, index, currSubset, result):

		if index == len(nums):

			result.append(currSubset.copy())
			return

		currSubset.append(nums[index])

		self.helper(nums, index+1, currSubset, result)

		currSubset.pop()

		while index < len(nums)-1 and nums[index] == nums[index+1]:
			index += 1

		self.helper(nums, index+1, currSubset, result)

		