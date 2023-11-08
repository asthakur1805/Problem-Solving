class Solution:

	def lowestCommonAncestor(self,root,firstNode,secondNode):

		self.firstPath, self.secondPath, builder = None, None, []

		self.helper(root,builder,firstNode,secondNode)

		firstIndex, secondIndex = 0, 0

		while firstIndex < len(self.firstPath) and secondIndex < len(self.secondPath) and self.firstPath[firstIndex] == self.secondPath[secondIndex]:

			result = self.firstPath[firstIndex]

			firstIndex += 1
			secondIndex += 1

		return result

	def helper(self,node,builder,firstNode,secondNode):

		if not node or (self.firstPath and self.secondPath):

			return

		builder.append(node)

		if node.val == firstNode.val:

			self.firstPath = builder.copy()

		if node.val == secondNode.val:

			self.secondPath = builder.copy()

		self.helper(node.left,builder,firstNode,secondNode)

		self.helper(node.right,builder,firstNode,secondNode)

		builder.pop()



		