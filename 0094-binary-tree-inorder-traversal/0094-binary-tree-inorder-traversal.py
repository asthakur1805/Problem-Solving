class Solution:

	def inorderTraversal(self, root):

		curr, result = root, []

		while curr:

			if not curr.left:

				result.append(curr.val)

				curr = curr.right

			else:

				prev = curr.left

				while prev.right and prev.right != curr:

					prev = prev.right

				if not prev.right:

					prev.right = curr

					curr = curr.left

				else:

					prev.right = None

					result.append(curr.val)

					curr = curr.right


		return result