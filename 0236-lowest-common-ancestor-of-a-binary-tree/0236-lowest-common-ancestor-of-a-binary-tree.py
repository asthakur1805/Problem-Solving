class Solution:

	def lowestCommonAncestor(self,root,firstNode,secondNode):

		if not root: return None
	
		if root.val in (firstNode.val,secondNode.val): return root

		leftNode, rightNode = self.lowestCommonAncestor(root.left,firstNode,secondNode), self.lowestCommonAncestor(root.right,firstNode,secondNode)

		if leftNode and rightNode: return root

		if not leftNode and not rightNode: return None

		return leftNode if leftNode else rightNode