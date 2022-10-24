class Solution:

	def removeNthFromEnd(self, head, N):

		currentNode, listLength = head, 0

		while currentNode:

			listLength += 1

			currentNode = currentNode.next

		if listLength == N:

			return head.next

		currentNode = head

		for _ in range(listLength-N-1):

			currentNode = currentNode.next


		currentNode.next = currentNode.next.next


		return head