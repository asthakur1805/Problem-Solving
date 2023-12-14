class Solution:

	def countPrimes(self,upperBound):

		if upperBound <= 2:

			return 0

		sieve = [True] * upperBound

		upperPrimeLimit = int(upperBound ** 0.5)
	
		for prime in range(2,upperPrimeLimit+1):

			if sieve[prime]:

				for composite in range(prime**2,upperBound,prime):

					sieve[composite] = False

		count = 0

		for num in range(2,upperBound):

			count += sieve[num]

		return count