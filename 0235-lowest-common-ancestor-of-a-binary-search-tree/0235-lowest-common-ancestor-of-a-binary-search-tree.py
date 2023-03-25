class Solution:

	def lowestCommonAncestor(self, root, firstNode, secondNode):

		curr = root

		while True:

			if firstNode.val < curr.val and secondNode.val < curr.val:

				curr = curr.left

			elif firstNode.val > curr.val and secondNode.val > curr.val:

				curr = curr.right

			else:

				return curr