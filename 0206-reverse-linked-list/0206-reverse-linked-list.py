class Solution:

	def reverseList(self, head):

		return self.helper(head, None)

	def helper(self, currNode, prevNode):

		if not currNode:

			return prevNode

		nextNode = currNode.next

		currNode.next = prevNode

		return self.helper(nextNode, currNode)