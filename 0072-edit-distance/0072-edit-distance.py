class Solution:

	def minDistance(self,firstStr,secondStr):

		return self.helper(firstStr,secondStr,len(firstStr),len(secondStr),{})

	def helper(self,firstStr,secondStr,firstIndex,secondIndex,cache):

		if firstIndex == 0: return secondIndex 
	
		if secondIndex == 0: return firstIndex

		if firstStr[firstIndex-1] == secondStr[secondIndex-1]: return self.helper(firstStr,secondStr,firstIndex-1,secondIndex-1,cache)

		if (firstIndex,secondIndex) in cache: return cache[(firstIndex,secondIndex)]

		insertion = self.helper(firstStr,secondStr,firstIndex,secondIndex-1,cache)
		deletion = self.helper(firstStr,secondStr,firstIndex-1,secondIndex,cache)
		replacement = self.helper(firstStr,secondStr,firstIndex-1,secondIndex-1,cache)

		cache[(firstIndex,secondIndex)] = 1 + min(insertion,deletion,replacement)
		return cache[(firstIndex,secondIndex)]
	