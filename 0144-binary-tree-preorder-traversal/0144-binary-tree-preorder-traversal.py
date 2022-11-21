class Solution:

	def preorderTraversal(self, root):

		result = []

		self.preorder(root, result)

		return result

	def preorder(self, node, result):

		if not node:

			return 

		result.append(node.val)

		self.preorder(node.left, result)

		self.preorder(node.right, result)

		
