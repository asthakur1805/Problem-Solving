class Solution:

	def diameterOfBinaryTree(self, root):

		if not root:

			return 0

		leftDepth, rightDepth = self.calculateDepth(root.left), self.calculateDepth(root.right)

		return max(leftDepth + rightDepth, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)) 

	def calculateDepth(self, node):

		if not node:

			return 0

		return 1 + max(self.calculateDepth(node.left), self.calculateDepth(node.right))
	