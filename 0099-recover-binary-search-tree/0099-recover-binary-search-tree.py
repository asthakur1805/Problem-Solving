class Solution:

	def recoverTree(self, root):

		if not root:

			return

		self.curr, self.prev, self.firstViolation, self.secondViolation = root, TreeNode(float('-inf')), None, None

		while self.curr:

			if not self.curr.left:

				self.checkViolations()

			else:

				rightmostOfLeft = self.curr.left

				while rightmostOfLeft.right and rightmostOfLeft.right != self.curr:

					rightmostOfLeft = rightmostOfLeft.right

				if not rightmostOfLeft.right:

					rightmostOfLeft.right = self.curr

					self.curr = self.curr.left

				else:

					rightmostOfLeft.right = None

					self.checkViolations()

		self.firstViolation.val, self.secondViolation.val = self.secondViolation.val, self.firstViolation.val

	def checkViolations(self):

		if not self.firstViolation and not(self.prev.val < self.curr.val):

			self.firstViolation = self.prev

		if self.firstViolation and not(self.prev.val < self.curr.val):

			self.secondViolation = self.curr

		self.prev = self.curr

		self.curr = self.curr.right

			

				
			