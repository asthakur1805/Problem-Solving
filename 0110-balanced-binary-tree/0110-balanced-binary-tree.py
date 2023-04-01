class Solution:

	def isBalanced(self, root):

		return self.helper(root)[0]

	def helper(self, node):

		if not node:

			return (True, 0)

		leftBalanced, leftDepth = self.helper(node.left)
		rightBalanced, rightDepth = self.helper(node.right)

		nodeBalanced = leftBalanced and rightBalanced and abs(leftDepth-rightDepth) <= 1
		nodeDepth = 1 + max(leftDepth, rightDepth)

		return (nodeBalanced, nodeDepth)
