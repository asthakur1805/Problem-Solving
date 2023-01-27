class Solution:

	def reverseString(self, inputStr):

		self.helper(inputStr, 0, len(inputStr)-1)

	def helper(self, inputStr, leftPointer, rightPointer):

		if leftPointer >= rightPointer:

			return

		inputStr[leftPointer], inputStr[rightPointer] = inputStr[rightPointer], inputStr[leftPointer]

		self.helper(inputStr, leftPointer + 1, rightPointer - 1)

		
	