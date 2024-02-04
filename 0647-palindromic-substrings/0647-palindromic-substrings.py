class Solution:

	def countSubstrings(self,inputStr):

		result = 0

		for index in range(len(inputStr)):

			start, end = index, index

			while start >= 0 and end < len(inputStr) and inputStr[start] == inputStr[end]:

				result += 1
				start -= 1
				end += 1

			start, end = index, index+1

			while start >= 0 and end < len(inputStr) and inputStr[start] == inputStr[end]:

				result += 1
				start -= 1
				end += 1

		return result