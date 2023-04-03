class Solution:

	def isSameTree(self, firstTreeNode, secondTreeNode):

		if not firstTreeNode and not secondTreeNode:

			return True

		if not firstTreeNode or not secondTreeNode or firstTreeNode.val != secondTreeNode.val:

			return False

		return self.isSameTree(firstTreeNode.left, secondTreeNode.left) and self.isSameTree(firstTreeNode.right, secondTreeNode.right)
		