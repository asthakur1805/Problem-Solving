class Solution:

	def recoverTree(self, root):

		self.prevNode, self.currNode, self.firstViolationNode, self.secondViolationNode = TreeNode(float('-inf')), root, None, None

		while self.currNode:

			if not self.currNode.left:

				self.helper()

			else:

				rightmostOfLeft = self.currNode.left

				while rightmostOfLeft.right and rightmostOfLeft.right != self.currNode:

					rightmostOfLeft = rightmostOfLeft.right

				if not rightmostOfLeft.right:

					rightmostOfLeft.right = self.currNode

					self.currNode = self.currNode.left

				else:

					rightmostOfLeft.right = None

					self.helper()


		self.firstViolationNode.val, self.secondViolationNode.val = self.secondViolationNode.val, self.firstViolationNode.val

	def helper(self):

		if not self.firstViolationNode and not(self.prevNode.val < self.currNode.val):

			self.firstViolationNode = self.prevNode

		if self.firstViolationNode and not(self.prevNode.val < self.currNode.val):

			self.secondViolationNode = self.currNode

		self.prevNode = self.currNode

		self.currNode = self.currNode.right



			
				
				