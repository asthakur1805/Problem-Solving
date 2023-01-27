class Solution:

	def reverseString(self, inputStr):

		leftPointer, rightPointer = 0, len(inputStr)-1

		while leftPointer < rightPointer:

			inputStr[leftPointer], inputStr[rightPointer] = inputStr[rightPointer], inputStr[leftPointer]

			leftPointer, rightPointer = leftPointer + 1, rightPointer - 1