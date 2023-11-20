class Solution:

	def kthSmallest(self,root,K):

		self.result, self.K = None, K

		self.helper(root)

		return self.result

	def helper(self,node):

		if not node or self.K == 0:

			return

		self.helper(node.left)

		self.K -= 1

		if self.K == 0: 

			self.result = node.val
			return

		self.helper(node.right)