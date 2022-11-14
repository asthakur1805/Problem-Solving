class Solution:
	
	def permute(self, nums):

		builder = []

		result = []

		numberMap = set()

		self.helper(nums, builder, numberMap, result)

		return result

	def helper(self, nums, builder, numberMap, result):

		if len(builder) == len(nums):

			result.append(builder.copy())

			return 

		for num in nums:

			if num not in numberMap:

				builder.append(num)
				numberMap.add(num)

				self.helper(nums, builder, numberMap, result)

				builder.pop()
				numberMap.remove(num)

		

			