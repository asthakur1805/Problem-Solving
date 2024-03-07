class Solution:

	def isInterleave(self,firstStr,secondStr,resultStr):

		if len(firstStr) + len(secondStr) != len(resultStr):

			return False

		return self.helper(firstStr,secondStr,resultStr,0,0,{})

	def helper(self,firstStr,secondStr,resultStr,firstIndex,secondIndex,cache):

		if firstIndex == len(firstStr) and secondIndex == len(secondStr):

			return True

		if (firstIndex,secondIndex) in cache:

			return cache[(firstIndex,secondIndex)]

		if firstIndex < len(firstStr) and firstStr[firstIndex] == resultStr[firstIndex+secondIndex] and self.helper(firstStr,secondStr,resultStr,firstIndex+1,secondIndex,cache):

			cache[(firstIndex,secondIndex)] = True
			return True

		if secondIndex < len(secondStr) and secondStr[secondIndex] == resultStr[firstIndex+secondIndex] and self.helper(firstStr,secondStr,resultStr,firstIndex,secondIndex+1,cache):

			cache[(firstIndex,secondIndex)] = True
			return True

		cache[(firstIndex,secondIndex)] = False
		return False