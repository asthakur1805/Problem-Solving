class Solution:

	def sumOfLeftLeaves(self,root):

		self.resultSum = 0

		self.preorder(root,False)

		return self.resultSum

	def preorder(self,node,isLeftNode):

		if not node:

			return

		if not node.left and not node.right and isLeftNode:

				self.resultSum += node.val

		self.preorder(node.left,True)

		self.preorder(node.right,False)