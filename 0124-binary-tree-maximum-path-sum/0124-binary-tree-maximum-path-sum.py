class Solution:

	def maxPathSum(self,root):

		return self.helper(root)[1]

	def helper(self,node):

		if not node:

			return (0,float('-inf'))

		(leftPathSum,leftMax), (rightPathSum,rightMax) = self.helper(node.left), self.helper(node.right)

		leftPathSum, rightPathSum = max(leftPathSum,0), max(rightPathSum,0)

		rootPathSum = node.val + max(leftPathSum,rightPathSum)
		rootMax = max(leftMax,rightMax,node.val+leftPathSum+rightPathSum)

		return (rootPathSum,rootMax)