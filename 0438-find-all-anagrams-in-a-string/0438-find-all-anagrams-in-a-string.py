class Solution:

	def findAnagrams(self,firstStr,secondStr):

		if len(secondStr) > len(firstStr):

			return

		firstStrCounts, secondStrCounts = {}, {}

		for index in range(len(secondStr)):

			firstChar, secondChar = firstStr[index], secondStr[index]

			firstStrCounts[firstChar] = firstStrCounts.get(firstChar,0) + 1
			secondStrCounts[secondChar] = secondStrCounts.get(secondChar,0) + 1

		start, result = 0, []

		for end in range(len(secondStr),len(firstStr)):

			if self.checkAnagrams(firstStrCounts,secondStrCounts):

				result.append(start)

			firstStrCounts[firstStr[end]] = firstStrCounts.get(firstStr[end],0) + 1
			firstStrCounts[firstStr[start]] -= 1

			start += 1

		if self.checkAnagrams(firstStrCounts,secondStrCounts):

			result.append(start)

		return result

	def checkAnagrams(self,firstMap,secondMap):

		for currChar in secondMap:

			if secondMap[currChar] != firstMap.get(currChar,0):

				return False

		return True

			
			
 