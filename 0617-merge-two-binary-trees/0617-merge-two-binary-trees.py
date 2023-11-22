class Solution:

	def mergeTrees(self,firstTreeNode,secondTreeNode):
	
		if not firstTreeNode and not secondTreeNode:

			return

		firstVal = firstTreeNode.val if firstTreeNode else 0
		secondVal = secondTreeNode.val if secondTreeNode else 0

		root = TreeNode(firstVal+secondVal)

		root.left = self.mergeTrees(firstTreeNode.left if firstTreeNode else None, secondTreeNode.left if secondTreeNode else None)

		root.right = self.mergeTrees(firstTreeNode.right if firstTreeNode else None, secondTreeNode.right if secondTreeNode else None)

		return root
		

		