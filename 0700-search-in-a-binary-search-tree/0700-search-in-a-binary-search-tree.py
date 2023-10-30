class Solution:

	def searchBST(self,root,inputVal):

		curr = root

		while curr:

			if curr.val == inputVal:

				break

			curr = curr.left if inputVal < curr.val else curr.right

		return curr

				 