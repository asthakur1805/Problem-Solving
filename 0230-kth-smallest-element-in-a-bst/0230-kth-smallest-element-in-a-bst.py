class Solution:

	def kthSmallest(self,root,K):

		curr, count = root, 0

		while curr:

			if not curr.left:

				count += 1

				if count == K:

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
					
					count += 1

					if count == K:

						return curr.val

					curr = curr.right

		
					
		