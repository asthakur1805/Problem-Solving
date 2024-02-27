class Solution:

	def countPrimes(self,upperBound):

		if upperBound <= 2:

			return 0

	
		sieve = [True]*upperBound

		for prime in range(2,int(upperBound**0.5)+1):

			if sieve[prime]:

				for composite in range(prime*prime,upperBound,prime):

					sieve[composite] = False

		result = 0

		for currNum in range(2,upperBound):

			result += sieve[currNum]

		return result
				