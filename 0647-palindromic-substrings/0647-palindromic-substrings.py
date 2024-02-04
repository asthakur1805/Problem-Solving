class Solution:

	def countSubstrings(self,inputStr):

		result = 0

		for start in range(len(inputStr)):

			for end in range(start,len(inputStr)):

				if self.isPalindrome(inputStr,start,end):

					result += 1

		return result

	def isPalindrome(self,inputStr,start,end):

		while start < end:

			if inputStr[start] != inputStr[end]:

				return False

			start += 1
			end -= 1

		return True