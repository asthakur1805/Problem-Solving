class Solution:

	def isValidBST(self, root):

		if not root:

			return True

		return self.helper(root.left, float('-inf'), root.val) and self.helper(root.right, root.val, float('inf')) and self.isValidBST(root.left) and self.isValidBST(root.right)

		
	def helper(self, node, leftBound, rightBound):

		if not node:

			return True

		if not(leftBound < node.val < rightBound):

			return False

		return self.helper(node.left, leftBound, rightBound) and self.helper(node.right, leftBound, rightBound)