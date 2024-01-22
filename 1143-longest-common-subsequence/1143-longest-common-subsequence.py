class Solution:

	def longestCommonSubsequence(self,firstStr,secondStr):

		return self.helper(firstStr,secondStr,len(firstStr)-1,len(secondStr)-1,{})

	def helper(self,firstStr,secondStr,firstIndex,secondIndex,cache):

		if firstIndex < 0 or secondIndex < 0:

			return 0

		if (firstIndex,secondIndex) in cache:

			return cache[(firstIndex,secondIndex)]

		if firstStr[firstIndex] == secondStr[secondIndex]:

			cache[(firstIndex,secondIndex)] = 1 + self.helper(firstStr,secondStr,firstIndex-1,secondIndex-1,cache)
			return cache[(firstIndex,secondIndex)]

		cache[(firstIndex,secondIndex)] = max(self.helper(firstStr,secondStr,firstIndex-1,secondIndex,cache),self.helper(firstStr,secondStr,firstIndex,secondIndex-1,cache))
		return cache[(firstIndex,secondIndex)]

		
		
