class Solution:

	def lowestCommonAncestor(self, root, firstNode, secondNode):

		self.firstNodePath, self.secondNodePath, builder = None, None, []

		self.helper(root, firstNode, secondNode, builder)

		firstIndex, secondIndex, result = 0, 0, None

		while firstIndex < len(self.firstNodePath) and secondIndex < len(self.secondNodePath) and self.firstNodePath[firstIndex] == self.secondNodePath[secondIndex]:

			result = self.firstNodePath[firstIndex]

			firstIndex += 1
			secondIndex += 1

		return result


	def helper(self, currNode, firstNode, secondNode, builder):

		if not currNode:

			return

		builder.append(currNode)

		if currNode.val == firstNode.val:

			self.firstNodePath = builder.copy()

		elif currNode.val == secondNode.val:

			self.secondNodePath = builder.copy()

		self.helper(currNode.left, firstNode, secondNode, builder)

		self.helper(currNode.right, firstNode, secondNode, builder)

		builder.pop()

	

		

		

	
