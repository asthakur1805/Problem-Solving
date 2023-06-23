class Solution:

	def isSubtree(self, root, subRoot):

		if not subRoot: return True

		if not root: return False

		if self.isSameTree(root, subRoot):

			return True

		return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

	def isSameTree(self, leftTreeNode, rightTreeNode):

		if not leftTreeNode and not rightTreeNode: return True

		if not leftTreeNode or not rightTreeNode or leftTreeNode.val != rightTreeNode.val: return False

		return self.isSameTree(leftTreeNode.left, rightTreeNode.left) and self.isSameTree(leftTreeNode.right, rightTreeNode.right)