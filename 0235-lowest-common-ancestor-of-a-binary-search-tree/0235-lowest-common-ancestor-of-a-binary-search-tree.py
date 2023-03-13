class Solution:

	def lowestCommonAncestor(self, root, firstTreeNode, secondTreeNode):

		resultTreeNode = root

		while True:

			if firstTreeNode.val < resultTreeNode.val and secondTreeNode.val < resultTreeNode.val:

				resultTreeNode = resultTreeNode.left

			elif firstTreeNode.val > resultTreeNode.val and secondTreeNode.val > resultTreeNode.val:

				resultTreeNode = resultTreeNode.right

			else:

				return resultTreeNode