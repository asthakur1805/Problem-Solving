class Solution:

	def partition(self,inputStr):

		builder, result = [], []

		self.dfs(inputStr,0,builder,result)

		return result
		
	def dfs(self,inputStr,start,builder,result):

		if start == len(inputStr):

			result.append(builder.copy())

			return 

		for end in range(start,len(inputStr)):

			if self.isPalindrome(inputStr,start,end):

				builder.append(inputStr[start:end+1])

				self.dfs(inputStr,end+1,builder,result)

				builder.pop()

	def isPalindrome(self,inputStr,start,end):

		while start < end:

			if inputStr[start] != inputStr[end]:

				return False

			start += 1
			end -= 1

		return True

