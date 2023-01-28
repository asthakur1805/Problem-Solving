class Solution:

	def sumNumbers(self, root):

		self.result = 0

		self.helper(root, pathSum=0)

		return self.result

	def helper(self, node, pathSum):

		if not node:

			return 0

		pathSum = pathSum * 10 + node.val

		if not node.left and not node.right:
			
			self.result += pathSum

		self.helper(node.left, pathSum)

		self.helper(node.right, pathSum)

			

		
			

		
			

		