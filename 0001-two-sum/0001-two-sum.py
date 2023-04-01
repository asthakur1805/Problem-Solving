class Solution:

	def twoSum(self, nums, target):

		visited = {}

		for index, value in enumerate(nums):

			diff = target - value

			if diff in visited:

				return [visited[diff], index]

			visited[value] = index

		return []