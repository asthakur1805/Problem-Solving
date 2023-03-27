class Solution:

	def isValidBST(self, root):

		return self.validate(root, float('-inf'), float('inf'))

	def validate(self, node, lowerBound, upperBound):

		if not node:

			return True

		if not(lowerBound < node.val < upperBound):

			return False

		return self.validate(node.left, lowerBound, node.val) and self.validate(node.right, node.val, upperBound)

		