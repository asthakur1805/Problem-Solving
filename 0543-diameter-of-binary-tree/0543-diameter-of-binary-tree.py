class Solution:

	def diameterOfBinaryTree(self, root):
	
		return self.helper(root)[0]

	def helper(self, node):

		# Diameter, MaxDepth

		if not node:

			return [0, 0]

		leftDiameter, leftDepth = self.helper(node.left)
		rightDiameter, rightDepth = self.helper(node.right)

		nodeDiameter = max(leftDiameter, rightDiameter, leftDepth+rightDepth)
		nodeDepth = 1 + max(leftDepth, rightDepth)

		return [nodeDiameter, nodeDepth]
		