class Solution:

	def divide(self, dividend, divisor):

		if dividend == -(1 << 31) and divisor == -1:

			return (1 << 31) - 1

		sign = 1 if (dividend > 0) == (divisor > 0) else -1

		dividend, divisor, quotient = abs(dividend), abs(divisor), 0

		while dividend - divisor >= 0:

			power = 0

			while dividend - (divisor << 1 << power) >= 0:

				power += 1

			quotient += (1 << power)

			dividend -= (divisor << power)

		return quotient * sign

