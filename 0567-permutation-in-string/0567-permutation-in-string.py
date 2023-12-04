class Solution:

	def checkInclusion(self,firstStr,secondStr):

		if len(firstStr) > len(secondStr): return False

		firstStrCounts, secondStrCounts = [0]*26, [0]*26

		for index in range(len(firstStr)):

			firstStrCounts[ord(firstStr[index])-ord('a')] += 1
			secondStrCounts[ord(secondStr[index])-ord('a')] += 1

		matches = 0

		for firstCount,secondCount in zip(firstStrCounts,secondStrCounts):

			matches += (firstCount == secondCount)

		start = 0

		for end in range(len(firstStr),len(secondStr)):

			if matches == 26: return True

			secondChar = secondStr[start]

			secondStrCounts[ord(secondChar)-ord('a')] -= 1

			if firstStrCounts[ord(secondChar)-ord('a')] == secondStrCounts[ord(secondChar)-ord('a')]: matches += 1
			elif firstStrCounts[ord(secondChar)-ord('a')] - 1 == secondStrCounts[ord(secondChar)-ord('a')]: matches -= 1

			secondChar = secondStr[end]

			secondStrCounts[ord(secondChar)-ord('a')] += 1

			if firstStrCounts[ord(secondChar)-ord('a')] == secondStrCounts[ord(secondChar)-ord('a')]: matches += 1
			elif firstStrCounts[ord(secondChar)-ord('a')] + 1 == secondStrCounts[ord(secondChar)-ord('a')]: matches -= 1

			start += 1

		return matches == 26



				
	