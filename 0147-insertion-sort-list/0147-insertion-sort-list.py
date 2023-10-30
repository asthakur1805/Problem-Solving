class ListNode:

	def __init__(self,val=0,next=None):

		self.val = val
		self.next = next


class Solution:

	def insertionSortList(self, head):

		dummy = ListNode(0,head)

		prev, curr = head, head.next

		while curr:

			if prev.val <= curr.val:

				prev, curr = prev.next, curr.next
				continue

			firstNode, secondNode = dummy, dummy.next

			while secondNode.val < curr.val:

				firstNode, secondNode = firstNode.next, secondNode.next

			prev.next = curr.next
			curr.next = secondNode
			firstNode.next = curr
			curr = prev.next

		return dummy.next
