class Solution:

	def buildTree(self, preorder, inorder):

		inorderMap = {value:index for index,value in enumerate(inorder)}

		preorderStart, preorderEnd, inorderStart, inorderEnd = 0, len(preorder)-1, 0, len(inorder)-1

		return self.helper(preorder, inorder, preorderStart, preorderEnd, inorderStart, inorderEnd, inorderMap)

		
	def helper(self, preorder, inorder, preorderStart, preorderEnd, inorderStart, inorderEnd, inorderMap):

		if inorderStart > inorderEnd or preorderStart > preorderEnd:

			return

		root = TreeNode(preorder[preorderStart])

		rootIndex = inorderMap[root.val]

		root.left = self.helper(preorder, inorder, preorderStart+1, preorderStart+rootIndex-inorderStart, inorderStart, rootIndex-1, inorderMap)

		root.right = self.helper(preorder, inorder, preorderStart+rootIndex-inorderStart+1, preorderEnd, rootIndex+1, inorderEnd, inorderMap)

		return root