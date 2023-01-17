class Solution:

	def reverseString(self, inputStr):

		self.reverse(inputStr, 0, len(inputStr)-1)
		
	
	def reverse(self, inputStr, leftPointer, rightPointer):

		if leftPointer >= rightPointer:

			return

		inputStr[leftPointer], inputStr[rightPointer] = inputStr[rightPointer], inputStr[leftPointer]

		self.reverse(inputStr, leftPointer+1, rightPointer-1)



