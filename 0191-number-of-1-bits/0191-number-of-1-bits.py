class Solution:

	def hammingWeight(self, num):

		result = 0

		while num:

			num = num & (num-1)

			result += 1

		return result