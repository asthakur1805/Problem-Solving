class Solution:

	def countSubstrings(self,inputStr):

		result = 0

		for index in range(len(inputStr)):

			result += self.countPalindromes(inputStr,index,index) + self.countPalindromes(inputStr,index,index+1)
		
		return result

	def countPalindromes(self,inputStr,start,end):

		result = 0

		while start >= 0 and end < len(inputStr) and inputStr[start] == inputStr[end]:

				result += 1
				start -= 1
				end += 1

		return result