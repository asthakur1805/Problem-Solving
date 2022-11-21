class Solution:

	def inorderTraversal(self, root):

		result = []

		self.inorder(root, result)

		return result

	def inorder(self, node, result):

		if not node:

			return 

		self.inorder(node.left, result)

		result.append(node.val)

		self.inorder(node.right, result)

	