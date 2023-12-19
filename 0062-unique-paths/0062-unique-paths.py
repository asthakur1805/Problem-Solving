class Solution:

	def uniquePaths(self,numRows,numColumns):

		totalItems = numRows+numColumns-2
		chosenItems = numRows-1

		result = 1

		for curr in range(chosenItems):

			result *= (totalItems - curr) / (curr + 1)

		return int(result+0.5)

			