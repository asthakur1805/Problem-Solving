class Solution:

	def isValidBST(self, root):

		return self.helper(root, float(-inf),float(inf))

	def helper(self, node, leftBound, rightBound):

		if not node:

			return True

		if not(leftBound < node.val < rightBound):

			return False

		return self.helper(node.left, leftBound, node.val) and self.helper(node.right, node.val, rightBound)