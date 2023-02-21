class Solution:

	def recoverTree(self, root):

		inorderResult = []

		self.inorder(root, inorderResult)

		inorderResult.sort()

		self.index, self.firstViolationNode, self.secondViolationNode = 0, None, None

		self.helper(root, inorderResult)

		self.firstViolationNode.val, self.secondViolationNode.val = self.secondViolationNode.val, self.firstViolationNode.val

	
	def inorder(self, node, result):

		if not node:

			return

		self.inorder(node.left, result)

		result.append(node.val)

		self.inorder(node.right, result)

	def helper(self, node, inorderResult):

		if not node:

			return

		self.helper(node.left, inorderResult)

		if node.val != inorderResult[self.index]:

			if not self.firstViolationNode:

				self.firstViolationNode = node

			else:

				self.secondViolationNode = node

		self.index += 1

		self.helper(node.right, inorderResult)

			

		