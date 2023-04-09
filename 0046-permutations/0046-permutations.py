class Solution:

	def permute(self, nums):

		visited, builder, result = set(), [], []

		self.helper(nums, builder, visited, result)

		return result

	def helper(self, nums, builder, visited, result):

		if len(builder) == len(nums):

			result.append(builder.copy())

			return

		for num in nums:

			if num not in visited:

				visited.add(num)
				builder.append(num)

				self.helper(nums, builder, visited, result)

				visited.remove(num)
				builder.pop()

		