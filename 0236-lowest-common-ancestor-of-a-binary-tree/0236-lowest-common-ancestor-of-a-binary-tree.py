class Solution:

	def lowestCommonAncestor(self, root, firstNode, secondNode):

		self.firstPath, self.secondPath = [], []

		builder = []

		self.helper(root, firstNode, secondNode, builder)

		firstIndex, secondIndex, result = 0, 0, None

		while firstIndex < len(self.firstPath) and secondIndex < len(self.secondPath) and self.firstPath[firstIndex] == self.secondPath[secondIndex]:

			result = self.firstPath[firstIndex]

			firstIndex, secondIndex = firstIndex+1, secondIndex+1

		return result

	def helper(self, node, firstNode, secondNode, builder):

		if not node:

			return

		builder.append(node)

		if node.val == firstNode.val:

			self.firstPath = builder.copy()

		if node.val == secondNode.val:

			self.secondPath = builder.copy()

		self.helper(node.left, firstNode, secondNode, builder)

		self.helper(node.right, firstNode, secondNode, builder)

		builder.pop()
		

				