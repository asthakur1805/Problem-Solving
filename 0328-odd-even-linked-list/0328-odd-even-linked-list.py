class Solution:

	def oddEvenList(self,head):

		if not head:

			return

		evenHead = head.next

		currOdd, currEven = head, evenHead

		while currEven and currEven.next:

			currOdd.next, currEven.next = currOdd.next.next, currEven.next.next
			currOdd, currEven = currOdd.next, currEven.next

		currOdd.next = evenHead

		return head