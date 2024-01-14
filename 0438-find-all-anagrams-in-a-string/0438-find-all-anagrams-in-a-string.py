class Solution:

	def findAnagrams(self,firstStr,secondStr):

		if len(secondStr) > len(firstStr):

			return []

		firstStrCounts, secondStrCounts = [0]*26, [0]*26

		for index in range(len(secondStr)):

			firstStrCounts[ord(firstStr[index])-ord('a')] += 1
			secondStrCounts[ord(secondStr[index])-ord('a')] += 1

		matches = 0

		for index in range(26):

			matches += (firstStrCounts[index] == secondStrCounts[index])

		start, result = 0, []

		for end in range(len(secondStr),len(firstStr)):

			self.checkAnagram(matches,result,start)

			index = ord(firstStr[end])-ord('a')
			firstStrCounts[index] += 1
			if firstStrCounts[index] == secondStrCounts[index]: matches += 1
			elif firstStrCounts[index] == secondStrCounts[index]+1: matches -= 1

			index = ord(firstStr[start])-ord('a')
			firstStrCounts[index] -= 1
			if firstStrCounts[index] == secondStrCounts[index]: matches += 1
			elif firstStrCounts[index] == secondStrCounts[index]-1: matches -= 1

			start += 1

		self.checkAnagram(matches,result,start)

		return result

	def checkAnagram(self,matches,result,start):

		if matches == 26:

			result.append(start)
