class Solution:

	def kthSmallest(self, root,K):

		self.K, self.result = K, None

		self.inorder(root)

		return self.result

	def inorder(self,node):

		if not node or self.K == 0:

			return

		self.inorder(node.left)

		self.K -= 1

		if self.K == 0:

			self.result = node.val
			return

		self.inorder(node.right)