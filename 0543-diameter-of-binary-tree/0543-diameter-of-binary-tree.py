class Solution:

	def diameterOfBinaryTree(self, root):

		if not root:

			return 0

		return max(self.calculateHeight(root.left)+self.calculateHeight(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

	def calculateHeight(self, node):

		if not node:

			return 0

		return 1 + max(self.calculateHeight(node.left), self.calculateHeight(node.right))

