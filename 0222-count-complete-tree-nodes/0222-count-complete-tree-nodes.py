class Solution:

	def countNodes(self,root):

		if not root:

			return 0

		leftDepth, rightDepth = 0, 0

		curr = root

		while curr:

			leftDepth += 1

			curr = curr.left

		curr = root

		while curr:

			rightDepth += 1

			curr = curr.right

		return (1 << leftDepth)-1 if leftDepth == rightDepth else 1 + self.countNodes(root.left) + self.countNodes(root.right)


		

			