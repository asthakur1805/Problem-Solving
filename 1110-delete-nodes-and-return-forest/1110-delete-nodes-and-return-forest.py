class Solution:

	def delNodes(self,root,toDelete):

		toDelete = set(toDelete)

		result = []

		self.helper(root,toDelete,result)

		if root and root.val not in toDelete:

			result.append(root)

		return result

	def helper(self,node,toDelete,result):

		if not node:

			return

		node.left, node.right = self.helper(node.left,toDelete,result), self.helper(node.right,toDelete,result)

		if node.val in toDelete:

			if node.left:

				result.append(node.left)

			if node.right:

				result.append(node.right)

			node.left, node.right = None, None

			return None

		return node

	

	