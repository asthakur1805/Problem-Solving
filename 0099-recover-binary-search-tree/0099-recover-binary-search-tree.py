class Solution:

	def recoverTree(self, root):

		prevNode, currNode, self.firstViolation, self.secondViolation = TreeNode(float('-inf')), root, None, None

		while currNode:

			if not currNode.left:

				self.checkViolations(prevNode, currNode)

				prevNode = currNode
				currNode = currNode.right

			else:

				rightmostOfLeft = currNode.left

				while rightmostOfLeft.right and rightmostOfLeft.right != currNode:
	
					rightmostOfLeft = rightmostOfLeft.right

				if not rightmostOfLeft.right:

					rightmostOfLeft.right = currNode

					currNode = currNode.left

				else:

					rightmostOfLeft.right = None

					self.checkViolations(prevNode, currNode)

					prevNode = currNode
					currNode = currNode.right

		self.firstViolation.val, self.secondViolation.val = self.secondViolation.val, self.firstViolation.val

		
	def checkViolations(self, prevNode, currNode):

		if not self.firstViolation and currNode.val < prevNode.val:

			self.firstViolation = prevNode

		if self.firstViolation and currNode.val < prevNode.val:

			self.secondViolation = currNode


			