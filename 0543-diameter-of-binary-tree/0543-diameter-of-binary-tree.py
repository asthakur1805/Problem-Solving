class Solution:

	def diameterOfBinaryTree(self, root):

		resultDiameter = [0]

		self.helper(root, resultDiameter)

		return resultDiameter[0]

	def helper(self, node, resultDiameter):

		if not node:

			return

		leftHeight, rightHeight = self.calculateHeight(node.left), self.calculateHeight(node.right)

		resultDiameter[0] = max(resultDiameter[0], leftHeight + rightHeight)

		self.helper(node.left, resultDiameter)

		self.helper(node.right, resultDiameter)


	def calculateHeight(self, node):

		if not node:

			return 0

		return 1 + max(self.calculateHeight(node.left), self.calculateHeight(node.right))

		