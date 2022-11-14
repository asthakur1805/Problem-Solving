class Solution:

	def pathSum(self, root, target):

		builder = []

		result = []

		self.helper(root, target, builder, result)

		return result

	def helper(self, root, target, builder, result):

		if not root:

			return

		if not root.left and not root.right and root.val == target:
			
			builder.append(root.val)
			result.append(builder.copy())
			builder.pop()
			
			return

		builder.append(root.val)
		self.helper(root.left, target-root.val, builder, result)
		self.helper(root.right, target-root.val, builder, result)
		builder.pop()
			
		