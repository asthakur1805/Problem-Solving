class Solution:

	def isPalindrome(self, head):

		numsList = []

		curr = head

		while curr:

			numsList.append(curr.val)

			curr = curr.next

		left, right = 0, len(numsList)-1

		while left < right:

			if numsList[left] != numsList[right]:

				return False

			left, right = left + 1, right - 1

		return True