class Solution:

	def diameterOfBinaryTree(self, root):

		return self.helper(root)[0]
		
	def helper(self, node):

		# Returns a tuple(diameter, height)

		if not node:

			return (0, 0)

		leftDiameter, leftHeight = self.helper(node.left)

		rightDiameter, rightHeight = self.helper(node.right)

		nodeDiameter = max(leftDiameter, rightDiameter, leftHeight+rightHeight)

		return (nodeDiameter, 1 + max(leftHeight, rightHeight))