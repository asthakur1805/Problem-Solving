class Solution:

	def reverseList(self, head):

		prevNode, currNode = None, head

		while currNode:

			nextNode = currNode.next

			currNode.next = prevNode

			prevNode = currNode

			currNode = nextNode

		return prevNode