class Solution:

	def lowestCommonAncestor(self, root, firstNode, secondNode):

		if not root: return

		if root.val == firstNode.val or root.val == secondNode.val: return root

		leftResult, rightResult = self.lowestCommonAncestor(root.left, firstNode, secondNode), self.lowestCommonAncestor(root.right, firstNode, secondNode)

		if not leftResult and not rightResult: return

		if leftResult and rightResult: return root

		return leftResult if leftResult else rightResult