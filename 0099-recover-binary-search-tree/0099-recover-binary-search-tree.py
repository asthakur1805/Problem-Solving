class Solution:

	def recoverTree(self, root):

		inorderResult = []

		self.inorder(root, inorderResult)

		inorderResult.sort()

		self.index, self.firstViolation, self.secondViolation = 0, None, None

		self.checkViolations(root, inorderResult)

		self.firstViolation.val, self.secondViolation.val = self.secondViolation.val, self.firstViolation.val 

	def inorder(self, node, inorderResult):

		if not node:

			return

		self.inorder(node.left, inorderResult)

		inorderResult.append(node.val)

		self.inorder(node.right, inorderResult)

	def checkViolations(self, node, inorderResult):

		if not node:

			return

		self.checkViolations(node.left, inorderResult)

		if inorderResult[self.index] != node.val:

			if not self.firstViolation:

				self.firstViolation = node

			else:

				self.secondViolation = node

		self.index += 1

		self.checkViolations(node.right, inorderResult)

	