class Solution:

	def reverseString(self, inputStr):

		self.helper(inputStr, 0, len(inputStr)-1)

	def helper(self, inputStr, left, right):

		if left >= right:

			return

		inputStr[left], inputStr[right] = inputStr[right], inputStr[left]

		self.helper(inputStr, left+1, right-1)