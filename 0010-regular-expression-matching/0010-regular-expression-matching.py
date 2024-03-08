class Solution:

	def isMatch(self,inputStr,pattern):

		return self.helper(inputStr,pattern,0,0)

	def helper(self,inputStr,pattern,strIndex,patIndex):

		if strIndex >= len(inputStr) and patIndex >= len(pattern):

			return True

		if patIndex >= len(pattern):

			return False

		match = strIndex < len(inputStr) and (inputStr[strIndex] == pattern[patIndex] or pattern[patIndex] == '.')

		if patIndex+1 < len(pattern) and pattern[patIndex+1] == '*':

			return self.helper(inputStr,pattern,strIndex,patIndex+2) or match and self.helper(inputStr,pattern,strIndex+1,patIndex)

		if match:

			return self.helper(inputStr,pattern,strIndex+1,patIndex+1)

		return False

		