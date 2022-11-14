class Solution:

	def combine(self, n, k):

		builder = []

		result = []

		self.helper(1, n, k, builder, result)

		return result

	def helper(self, start, n, k, builder, result):

		if len(builder) == k:
			
			result.append(builder.copy())
			return

		for num in range(start, n+1):

			builder.append(num)

			self.helper(num+1, n, k, builder, result)

			builder.pop()

	

