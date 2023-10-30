class Solution:

	def longestPalindrome(self,inputStr):

		evenCharacterCount, charSet = 0, set()

		for char in inputStr:

			if char not in charSet:

				charSet.add(char)

			else:

				charSet.remove(char)

				evenCharacterCount += 1

		return 2 * evenCharacterCount if not charSet else 2 * evenCharacterCount + 1