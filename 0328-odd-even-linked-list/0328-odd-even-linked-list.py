class Solution:

	def oddEvenList(self, head):

		if not head:

			return 

		headEven = head.next

		currOdd, currEven = head, headEven

		while True:

			if not currOdd or not currOdd.next:
		
				break

			currOdd.next = currOdd.next.next
			currOdd = currOdd.next

			if not currEven or not currEven.next:

				break

			currEven.next = currEven.next.next
			currEven = currEven.next

		tailOdd = head

		while tailOdd.next:

			tailOdd = tailOdd.next

		tailOdd.next = headEven

		return head