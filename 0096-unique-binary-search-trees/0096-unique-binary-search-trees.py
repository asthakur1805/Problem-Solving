class Solution:

	def numTrees(self,upperBound):

		return self.helper(upperBound,{})

	def helper(self,upperBound,cache):

		if upperBound <= 1:

			return 1

		if upperBound in cache:

			return cache[upperBound]

		for index in range(1,upperBound+1):

			cache[upperBound] = cache.get(upperBound,0) + self.helper(index-1,cache) * self.helper(upperBound-index,cache)

		return cache[upperBound]