class Solution:

	def isPalindrome(self, head):

		nums = []

		while head:

			nums.append(head.val)

			head = head.next

		leftPointer, rightPointer = 0, len(nums)-1

		while leftPointer <= rightPointer:

			if nums[leftPointer] != nums[rightPointer]:

				return False

			leftPointer += 1

			rightPointer -= 1

		return True