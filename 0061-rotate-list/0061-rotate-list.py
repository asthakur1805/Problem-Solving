class Solution:

	def rotateRight(self, head, numRotations):

		nums = []

		curr = head

		while curr:

			nums.append(curr.val)

			curr = curr.next

		curr = head

		for index in range(len(nums)):

			nums[(index+numRotations)%len(nums)] = curr.val

			curr = curr.next

		curr = head

		for num in nums:

			curr.val = num

			curr = curr.next

		return head