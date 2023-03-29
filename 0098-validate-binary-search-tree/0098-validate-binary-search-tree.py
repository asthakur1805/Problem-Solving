class Solution:

	def isValidBST(self, root):

		return self.helper(root, float('-inf'), float('inf'))

	def helper(self, node, lowerBound, upperBound):

		if not node:

			return True

		if not(lowerBound < node.val < upperBound):

			return False

		return self.helper(node.left, lowerBound, node.val) and self.helper(node.right, node.val, upperBound)