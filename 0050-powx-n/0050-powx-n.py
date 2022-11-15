class Solution:

	def myPow(self, base, exponent):

		result = self.helper(base, abs(exponent))

		return 1 / result if exponent < 0 else result

	def helper(self, base, exponent):

		if exponent == 0:
			return 1

		if base in (0,1):
			return base

		result = self.helper(base * base, exponent // 2)

		return result * base if exponent % 2 else result
	