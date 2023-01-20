class Solution:

	def singleNumber(self, nums):

		counts = {}

		for num in nums:

			counts[num] = counts.get(num, 0) + 1

		result = []

		for num, count in counts.items():

			if count == 1:

				result.append(num)


		return result

		