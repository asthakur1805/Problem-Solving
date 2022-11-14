class Solution:

	def pathSum(self, root, target):

		builder = []

		result = []

		self.helper(root, target, builder, result)

		return result

	def helper(self, root, target, builder, result):

		if not root:

			return

		builder.append(root.val)

		if not root.left and not root.right and root.val == target:
			
			result.append(builder.copy())
			builder.pop()
			return

		self.helper(root.left, target-root.val, builder, result)
		self.helper(root.right, target-root.val, builder, result)
		
		builder.pop()
			
		