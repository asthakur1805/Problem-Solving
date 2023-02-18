class Solution:

	def hammingWeight(self, number):

		count = 0

		while number:

			number &= (number-1)

			count += 1

		return count