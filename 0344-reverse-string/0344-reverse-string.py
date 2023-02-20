class Solution:

	def reverseString(self, inputStr):

		left, right = 0, len(inputStr)-1

		while left < right:

			inputStr[left], inputStr[right] = inputStr[right], inputStr[left]

			left, right = left+1, right-1

		