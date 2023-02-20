class Solution:

	def diameterOfBinaryTree(self, root):

		self.resultDiameter = 0

		self.helper(root)

		return self.resultDiameter
		
	def helper(self, node):

		if not node:

			return 0

		leftDepth, rightDepth = self.helper(node.left), self.helper(node.right)

		self.resultDiameter = max(self.resultDiameter, leftDepth + rightDepth)

		return 1 + max(leftDepth, rightDepth)