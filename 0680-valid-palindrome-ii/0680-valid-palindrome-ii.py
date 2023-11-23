class Solution:

	def validPalindrome(self,inputStr):

		left, right = 0, len(inputStr)-1

		while left < right:

			if inputStr[left] != inputStr[right]:

				return self.isPalindrome(inputStr,left+1,right) or self.isPalindrome(inputStr,left,right-1)

			left += 1

			right -= 1

		return True

	def isPalindrome(self,inputStr,left,right):

		while left < right:

			if inputStr[left] != inputStr[right]:

				return False

			left += 1

			right -= 1

		return True