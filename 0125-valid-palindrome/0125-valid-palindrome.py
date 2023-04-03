class Solution:

	def isPalindrome(self, inputStr):

		left, right = 0, len(inputStr)-1

		while left < right:

			while left < right and not self.isAlphaNumeric(inputStr[left]):

				left += 1

			while left < right and not self.isAlphaNumeric(inputStr[right]):

				right -= 1

			if inputStr[left].lower() != inputStr[right].lower():

				return False

			left, right = left + 1, right - 1

		return True

	def isAlphaNumeric(self, char):

		return ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9')