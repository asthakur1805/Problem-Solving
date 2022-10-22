class Solution:

	def middleNode(self, head):

		listLength  = 0

		currNode = head

		while currNode:

			listLength += 1

			currNode = currNode.next

		currNode = head

		for _ in range(listLength // 2):

			currNode = currNode.next

		return currNode