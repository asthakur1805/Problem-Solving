class Solution:

	def twoSum(self, inputNums, target):

		left, right = 0, len(inputNums) - 1

		while left < right:

			addition = inputNums[left] + inputNums[right]

			if addition == target:

				return [left+1, right+1]

			if addition < target:

				left += 1

			else:

				right -= 1

		return []
		