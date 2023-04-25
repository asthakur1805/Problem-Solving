class Solution:

	def buildTree(self, inorder, postorder):

		inorderStart, inorderEnd, postorderStart, postorderEnd = 0, len(inorder)-1, 0, len(postorder)-1

		inorderMap = {num:index for index, num in enumerate(inorder)}

		return self.helper(inorder, postorder, inorderStart, inorderEnd, postorderStart, postorderEnd, inorderMap)

	def helper(self, inorder, postorder, inorderStart, inorderEnd, postorderStart, postorderEnd, inorderMap):

		if inorderStart > inorderEnd or postorderStart > postorderEnd:

			return

		root = TreeNode(postorder[postorderEnd])

		mid = inorderMap[postorder[postorderEnd]]

		root.left = self.helper(inorder, postorder, inorderStart, mid-1, postorderStart, postorderEnd-inorderEnd+mid-1, inorderMap)

		root.right = self.helper(inorder, postorder, mid+1, inorderEnd, postorderEnd-inorderEnd+mid, postorderEnd-1, inorderMap)

		return root