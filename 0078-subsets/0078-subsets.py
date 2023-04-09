class Solution:

	def subsets(self, nums):

		index, currSubset, result = 0, [], []

		self.helper(nums, index, currSubset, result)

		return result

	def helper(self, nums, index, currSubset, result):

		if index == len(nums):

			result.append(currSubset.copy())
			return

		currSubset.append(nums[index])

		self.helper(nums, index+1, currSubset, result)

		currSubset.pop()

		self.helper(nums, index+1, currSubset, result)
