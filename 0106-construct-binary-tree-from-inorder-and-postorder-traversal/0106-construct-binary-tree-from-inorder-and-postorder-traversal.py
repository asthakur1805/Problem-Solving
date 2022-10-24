class Solution:

	def buildTree(self, inorder, postorder):

		inorderMap = {value:index for index,value in enumerate(inorder)}

		inorderStart, inorderEnd, postorderStart, postorderEnd = 0, len(inorder)-1, 0, len(postorder)-1

		return self.helper(inorder, postorder, inorderStart, inorderEnd, postorderStart, postorderEnd, inorderMap)

	def helper(self, inorder, postorder, inorderStart, inorderEnd, postorderStart, postorderEnd, inorderMap):

		if inorderStart > inorderEnd or postorderStart > postorderEnd:

			return

		rootNode = TreeNode(postorder[postorderEnd])

		rootIndex = inorderMap[rootNode.val]

		rootNode.left = self.helper(inorder, postorder, inorderStart, rootIndex-1, postorderStart, postorderEnd-inorderEnd+rootIndex-1, inorderMap)

		rootNode.right = self.helper(inorder, postorder, rootIndex+1, inorderEnd, postorderEnd-inorderEnd+rootIndex, postorderEnd-1, inorderMap)

		return rootNode
	