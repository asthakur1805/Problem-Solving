class Solution:

	def delNodes(self,root,to_delete):

		result = []

		to_delete = set(to_delete)

		self.helper(root,to_delete,result)

		if root.val not in to_delete:

			result.append(root)

		return result

	def helper(self,node,to_delete,result):

		if not node:

			return

		node.left = self.helper(node.left,to_delete,result)

		node.right = self.helper(node.right,to_delete,result)

		if node.val in to_delete:

			if node.left:

				result.append(node.left)

			if node.right:

				result.append(node.right)

			return

		else:

			return node

		