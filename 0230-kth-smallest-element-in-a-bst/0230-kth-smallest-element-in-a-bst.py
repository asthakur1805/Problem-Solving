class Solution:

	def kthSmallest(self,root,K):

		curr = root

		while curr:

			if not curr.left:

				K -= 1

				if K == 0:

					return curr.val

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

					K -= 1

					if K == 0:

						return curr.val

					curr = curr.right
