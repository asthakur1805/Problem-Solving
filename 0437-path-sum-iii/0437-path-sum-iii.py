class Solution:

	def pathSum(self,root,targetSum):

		self.result = 0

		self.preorder(root,targetSum)

		return self.result

	def preorder(self,node,targetSum):

		if not node:

			return 

		self.countPaths(node,targetSum)

		self.preorder(node.left,targetSum)

		self.preorder(node.right,targetSum)

	def countPaths(self,node,targetSum):

		if not node:

			return 

		if node.val == targetSum:

			self.result += 1

		self.countPaths(node.left,targetSum-node.val)

		self.countPaths(node.right,targetSum-node.val)