class Solution:

	def generateTrees(self,upperBound):

		return self.buildTrees(1,upperBound,{})

	def buildTrees(self,left,right,cache):

		if left > right:

			return [None]

		result = []

		if (left,right) in cache:

			return cache[(left,right)]

		for nodeVal in range(left,right+1):

			for leftSubTree in self.buildTrees(left,nodeVal-1,cache):

				for rightSubTree in self.buildTrees(nodeVal+1,right,cache):

					result.append(TreeNode(nodeVal,leftSubTree,rightSubTree))

		cache[(left,right)] = result
		return result