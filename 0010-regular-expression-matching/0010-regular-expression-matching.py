class Solution:

	def isMatch(self,inputStr,pattern):

		return self.helper(inputStr,pattern,0,0,{})

	def helper(self,inputStr,pattern,strIndex,patIndex,cache):

		if strIndex == len(inputStr) and patIndex == len(pattern):

			return True

		if patIndex == len(pattern):

			return False

		if (strIndex,patIndex) in cache:

			return cache[(strIndex,patIndex)]

		match = strIndex < len(inputStr) and (inputStr[strIndex] == pattern[patIndex] or pattern[patIndex] == '.')

		if patIndex+1<len(pattern) and pattern[patIndex+1] == '*':

			cache[(strIndex,patIndex)] = self.helper(inputStr,pattern,strIndex,patIndex+2,cache) or match and self.helper(inputStr,pattern,strIndex+1,patIndex,cache)
			return cache[(strIndex,patIndex)]

		if match:

			cache[(strIndex,patIndex)] = self.helper(inputStr,pattern,strIndex+1,patIndex+1,cache)
			return cache[(strIndex,patIndex)]

		cache[(strIndex,patIndex)] = False
		return False