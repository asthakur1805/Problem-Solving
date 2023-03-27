class Solution:

	def recoverTree(self, root):

		self.former, self.curr, self.firstViolation, self.secondViolation = TreeNode(float('-inf')), root, None, None

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

		self.firstViolation.val, self.secondViolation.val = self.secondViolation.val, self.firstViolation.val


	def checkViolations(self):

		if not self.firstViolation and not(self.former.val < self.curr.val):

				self.firstViolation = self.former
	
		if self.firstViolation and not(self.former.val < self.curr.val):

				self.secondViolation = self.curr

		self.former = self.curr
		self.curr = self.curr.right
				