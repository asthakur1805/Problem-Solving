class Solution:

	def diameterOfBinaryTree(self, root):

		return self.helper(root)[0]

	def helper(self, node):

		if not node:

			# Diameter, Depth
			return (0, 0)

		leftDiameter, leftDepth = self.helper(node.left)

		rightDiameter, rightDepth = self.helper(node.right)

		resultDiameter = max(leftDiameter, rightDiameter, leftDepth+rightDepth)

		resultDepth = 1 + max(leftDepth, rightDepth)

		return (resultDiameter, resultDepth)
	