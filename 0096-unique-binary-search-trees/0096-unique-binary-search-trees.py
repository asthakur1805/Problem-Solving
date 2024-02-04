class Solution:

	def numTrees(self,upperBound):

		return int((self.combinations(2*upperBound,upperBound) / (upperBound + 1)) + 0.5) 

	def combinations(self,totalItems,chosenItems):

		result = 1

		for index in range(chosenItems):

			result *= (totalItems-index) / (index+1)

		return result