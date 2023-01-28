class Solution:

	def isValidBST(self, root):

		if not root:

			return True

		return self.helper(root.left, float('-inf'),root.val) and self.helper(root.right, root.val, float('inf')) and self.isValidBST(root.left) and self.isValidBST(root.right)

		
	def helper(self, node, lowerBound, upperBound):

		if not node:

			return True

		if not(lowerBound < node.val < upperBound):

			return False

		return self.helper(node.left, lowerBound, upperBound) and self.helper(node.right, lowerBound, upperBound)