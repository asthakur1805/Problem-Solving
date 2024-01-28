class Solution:

	def isMatch(self,firstStr,secondStr):

		return self.helper(firstStr,secondStr,len(firstStr)-1,len(secondStr)-1,{})

	def helper(self,firstStr,secondStr,firstIndex,secondIndex,cache):

		if firstIndex < 0 and secondIndex < 0:

			return True

		if secondIndex < 0:

			return False

		if firstIndex < 0:

			for currIndex in range(secondIndex+1):

				if secondStr[currIndex] != '*':

					return False

			return True

		if (firstIndex,secondIndex) in cache:

			return cache[(firstIndex,secondIndex)]

		if firstStr[firstIndex] == secondStr[secondIndex] or secondStr[secondIndex] == '?':

			cache[(firstIndex,secondIndex)] = self.helper(firstStr,secondStr,firstIndex-1,secondIndex-1,cache)
			return cache[(firstIndex,secondIndex)]

		if secondStr[secondIndex] == '*':

			cache[(firstIndex,secondIndex)] = self.helper(firstStr,secondStr,firstIndex,secondIndex-1,cache) or self.helper(firstStr,secondStr,firstIndex-1,secondIndex,cache)
			return cache[(firstIndex,secondIndex)]

		cache[(firstIndex,secondIndex)] = False
		return cache[(firstIndex,secondIndex)]

			

			