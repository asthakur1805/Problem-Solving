class Solution:

	def sortList(self,head):

		if not head:

			return 

		return self.mergeSort(head)

	def mergeSort(self, head):

		prev, slow, fast = None, head, head

		while fast and fast.next:

			prev = slow
			slow = slow.next
			fast = fast.next.next

		if slow == head:

			return head

		prev.next = None

		dummy = ListNode(0)

		currResultList, currLeftList, currRightList = dummy, self.mergeSort(head), self.mergeSort(slow)


		while currLeftList and currRightList:
			
			if currLeftList.val <= currRightList.val:

				currResultList.next = currLeftList
				currLeftList = currLeftList.next

			else:

				currResultList.next = currRightList
				currRightList = currRightList.next

			currResultList = currResultList.next

		currResultList.next = currLeftList if currLeftList else currRightList

		return dummy.next
		

		