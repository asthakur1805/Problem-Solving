class Solution:

	def countNodes(self,root):

		if not root:

			return 0

		leftHeight, rightHeight = 0, 0

		curr = root

		while curr:

			leftHeight += 1

			curr = curr.left

		curr = root

		while curr:

			rightHeight += 1

			curr = curr.right

		if leftHeight == rightHeight: return (1<<leftHeight) - 1

		return 1 + self.countNodes(root.left) + self.countNodes(root.right)