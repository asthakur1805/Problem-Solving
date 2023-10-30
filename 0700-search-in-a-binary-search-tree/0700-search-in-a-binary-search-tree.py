class Solution:

	def searchBST(self,root,inputVal):

		if not root:

			return

		if root.val == inputVal:

			return root

		return self.searchBST(root.left,inputVal) if inputVal < root.val else self.searchBST(root.right,inputVal)

				 