class Solution:

	def countBits(self,upperBound):

		cache, offset = [0], 1

		for num in range(1,upperBound+1):

			if (offset << 1) == num:

				offset <<= 1

			cache.append(cache[num-offset]+1)

		return cache

			

		
			