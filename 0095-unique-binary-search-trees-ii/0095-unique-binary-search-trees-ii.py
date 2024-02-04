class Solution:

	def generateTrees(self,upperBound):

		return self.buildTrees(1,upperBound)

	def buildTrees(self,left,right):

		if left > right:

			return [None]

		result = []

		for nodeVal in range(left,right+1):

			for leftSubTree in self.buildTrees(left,nodeVal-1):

				for rightSubTree in self.buildTrees(nodeVal+1,right):

					result.append(TreeNode(nodeVal,leftSubTree,rightSubTree))

		return result