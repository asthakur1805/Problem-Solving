class Solution:

	def divide(self, dividend, divisor):

		sign, boundary = 1, (1 << 31) - 1

		if (dividend > 0) != (divisor > 0):
			
			sign, boundary = -1, boundary+1

		dividend, divisor, quotient = abs(dividend), abs(divisor), 0

		while dividend - divisor >= 0:

			power = 0

			while dividend - (divisor << (power + 1)) >= 0:

				power += 1
				
				print(dividend)
				print(power)

			if quotient + (1 << power) > boundary:

				return sign * boundary

			quotient += (1 << power)

			dividend -= (divisor << power)

		return quotient * sign

			
	

		