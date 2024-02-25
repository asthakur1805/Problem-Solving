class Solution:

	def minimumTotal(self,triangle):

		return self.helper(triangle,0,0,{})

	def helper(self,triangle,currRow,currColumn,cache):

		if (currRow,currColumn) in cache:

			return cache[(currRow,currColumn)]

		result = triangle[currRow][currColumn]

		if currRow < len(triangle)-1:

			down = self.helper(triangle,currRow+1,currColumn,cache)
			downRight = self.helper(triangle,currRow+1,currColumn+1,cache)

			result += min(down,downRight)

		cache[(currRow,currColumn)] = result
		return result