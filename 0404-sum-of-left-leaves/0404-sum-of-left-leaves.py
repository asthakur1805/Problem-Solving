class Solution:

	def sumOfLeftLeaves(self,root):

		self.resultSum = 0
	
		self.helper(root,False)

		return self.resultSum

	def helper(self,node,isLeftSubtree):

		if not node:

			return

		if not node.left and not node.right and isLeftSubtree:

			self.resultSum += node.val

		self.helper(node.left,True)

		self.helper(node.right,False)