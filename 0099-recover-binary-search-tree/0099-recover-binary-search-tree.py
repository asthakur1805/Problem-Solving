
class Solution:
	
	def recoverTree(self, root):

		self.firstViolationNode, self.secondViolationNode, self.index = None, None, 0
		
		inorderResult = []

		self.inorderBuilder(root, inorderResult)

		inorderResult.sort()

		self.violationDetector(root, inorderResult)

		self.firstViolationNode.val, self.secondViolationNode.val = self.secondViolationNode.val, self.firstViolationNode.val

	def inorderBuilder(self, node, inorderResult):

		if not node:

			return 

		self.inorderBuilder(node.left, inorderResult)

		inorderResult.append(node.val)

		self.inorderBuilder(node.right, inorderResult)

	def violationDetector(self, node, inorderResult):

		if not node:

			return 

		self.violationDetector(node.left, inorderResult)

		if node.val != inorderResult[self.index]:

			if not self.firstViolationNode:

				self.firstViolationNode = node

			else:

				self.secondViolationNode = node

		self.index += 1

		self.violationDetector(node.right, inorderResult)



	
