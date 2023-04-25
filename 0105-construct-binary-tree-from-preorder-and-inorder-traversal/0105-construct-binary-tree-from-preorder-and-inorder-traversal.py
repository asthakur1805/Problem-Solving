class Solution:

	def buildTree(self, preorder, inorder):

		inorderStart, inorderEnd, preorderStart, preorderEnd = 0, len(inorder)-1, 0, len(preorder)-1

		inorderMap = {num: index for index, num in enumerate(inorder)}

		return self.helper(preorder, inorder, preorderStart, preorderEnd, inorderStart, inorderEnd, inorderMap)

	def helper(self, preorder, inorder, preorderStart, preorderEnd, inorderStart, inorderEnd, inorderMap):

		if preorderStart > preorderEnd or inorderStart > inorderEnd:

			return

		root = TreeNode(preorder[preorderStart])

		mid = inorderMap[preorder[preorderStart]]

		root.left = self.helper(preorder, inorder, preorderStart+1, preorderStart+mid-inorderStart, inorderStart, mid-1, inorderMap)

		root.right = self.helper(preorder, inorder, preorderStart+mid-inorderStart+1, preorderEnd, mid+1, inorderEnd, inorderMap)

		return root
	

		