class Solution:

	def copyRandomList(self, head):

		if not head:

			return

		originalToCopied = {}

		originalNode = head

		while originalNode:

			copiedNode = ListNode(originalNode.val)

			originalToCopied[originalNode] = copiedNode

			originalNode = originalNode.next

		originalNode = head

		resultHead = originalToCopied[originalNode]

		while originalNode:
			
			copiedNode = originalToCopied[originalNode]

			copiedNode.next = originalToCopied.get(originalNode.next,None)
			copiedNode.random = originalToCopied.get(originalNode.random, None)

			originalNode = originalNode.next

		return resultHead