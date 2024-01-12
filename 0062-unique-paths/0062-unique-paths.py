class Solution:

	def uniquePaths(self,numRows,numColumns):

		totalItems, chosenItems, result = numRows+numColumns-2, numRows-1, 1

		for curr in range(chosenItems):

			result *= (totalItems - curr) / (curr + 1)

		return int(round(result,1))