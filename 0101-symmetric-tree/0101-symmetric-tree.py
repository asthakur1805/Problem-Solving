class Solution:

	def isSymmetric(self, root):

		return self.helper(root, root)

	def helper(self, leftTreeNode, rightTreeNode):

		if not leftTreeNode and not rightTreeNode:

			return True

		if not leftTreeNode or not rightTreeNode or leftTreeNode.val != rightTreeNode.val:

			return False

		return self.helper(leftTreeNode.left, rightTreeNode.right) and self.helper(leftTreeNode.right, rightTreeNode.left)


