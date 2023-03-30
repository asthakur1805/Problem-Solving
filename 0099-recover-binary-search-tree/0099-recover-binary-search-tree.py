class Solution:

	def recoverTree(self, root):

		self.former, self.curr, self.firstViolationNode, self.secondViolationNode = TreeNode(float('-inf')), root, None, None

		while self.curr:

			if not self.curr.left:

				self.checkViolations()

			else:

				prev = self.curr.left

				while prev.right and prev.right != self.curr:

					prev = prev.right

				if not prev.right:

					prev.right = self.curr

					self.curr = self.curr.left

				else:

					prev.right = None

					self.checkViolations()

		self.firstViolationNode.val, self.secondViolationNode.val = self.secondViolationNode.val, self.firstViolationNode.val

	def checkViolations(self):

		if not self.firstViolationNode and not(self.former.val < self.curr.val):

			self.firstViolationNode = self.former

		if self.firstViolationNode and not(self.former.val < self.curr.val):

			self.secondViolationNode = self.curr

		self.former = self.curr
		self.curr = self.curr.right