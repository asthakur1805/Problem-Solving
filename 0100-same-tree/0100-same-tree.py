class Solution:

	def isSameTree(self, firstRoot, secondRoot):

		stack = [(firstRoot, secondRoot)]

		while stack:

			firstTreeNode, secondTreeNode = stack.pop()

			if not firstTreeNode and not secondTreeNode:

				continue

			if not firstTreeNode or not secondTreeNode or firstTreeNode.val != secondTreeNode.val:

				return False

			stack.append((firstTreeNode.left, secondTreeNode.left))
			stack.append((firstTreeNode.right, secondTreeNode.right))

		return True