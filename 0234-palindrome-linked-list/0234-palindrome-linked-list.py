class Solution:

	def isPalindrome(self, head):

		numsList, curr = [], head

		while curr:

			numsList.append(curr.val)

			curr = curr.next

		leftPointer, rightPointer = 0, len(numsList)-1

		while leftPointer < rightPointer:

			if numsList[leftPointer] != numsList[rightPointer]:

					return False

			leftPointer, rightPointer = leftPointer + 1, rightPointer - 1

		return True
		