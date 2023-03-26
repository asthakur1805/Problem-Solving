class Solution:

	def copyRandomList(self, head):

		oldToNew = {None: None}

		curr = head

		while curr:

			oldToNew[curr] = ListNode(curr.val)

			curr = curr.next

		curr = head

		while curr:

			newNode = oldToNew[curr]

			newNode.next, newNode.random = oldToNew[curr.next], oldToNew[curr.random]

			curr = curr.next

		return oldToNew[head]