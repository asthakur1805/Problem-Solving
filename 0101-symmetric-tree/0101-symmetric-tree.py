class Solution:

	def isSymmetric(self, root):

		stack = [(root, root)]

		while stack:

			leftTreeNode, rightTreeNode = stack.pop()

			if not leftTreeNode and not rightTreeNode:

				continue

			if not leftTreeNode or not rightTreeNode or leftTreeNode.val != rightTreeNode.val:

				return False

			stack.append((leftTreeNode.left, rightTreeNode.right))

			stack.append((leftTreeNode.right, rightTreeNode.left))

		return True