class Solution:

	def hammingWeight(self, number):

		count = 0
	
		for bitPosition in range(32):

			if number & (1 << bitPosition):

				count += 1

		return count