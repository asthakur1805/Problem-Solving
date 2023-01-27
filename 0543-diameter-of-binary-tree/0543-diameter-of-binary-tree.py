class Solution:

	def diameterOfBinaryTree(self, root):

		if not root:

			return 0

		result = self.maxDepth(root.left) + self.maxDepth(root.right)

		return max(result, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

	def maxDepth(self, node):

		if not node:

			return 0

		return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))