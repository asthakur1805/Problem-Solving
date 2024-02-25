class Solution:

	def findAnagrams(self,firstStr,secondStr):

		if len(secondStr) > len(firstStr):

			return

		firstStrCounts, secondStrCounts = {}, {}

		for index in range(len(secondStr)):

			firstChar, secondChar = firstStr[index], secondStr[index]

			firstStrCounts[firstChar] = firstStrCounts.get(firstChar,0) + 1
			secondStrCounts[secondChar] = secondStrCounts.get(secondChar,0) + 1

		matches = 0

		for currVal in range(26):

			currChar = chr(currVal + ord('a'))

			if secondStrCounts.get(currChar,0) == firstStrCounts.get(currChar,0):

				matches += 1

		start, result = 0, []

		for end in range(len(secondStr),len(firstStr)):

			if matches == 26:

				result.append(start)

			currChar = firstStr[end]

			firstStrCounts[currChar] = firstStrCounts.get(currChar,0) + 1

			if firstStrCounts[currChar] == secondStrCounts.get(currChar,0):

				matches += 1

			elif firstStrCounts[currChar] == secondStrCounts.get(currChar,0) + 1:

				matches -= 1

			currChar = firstStr[start]

			firstStrCounts[currChar] -= 1

			if firstStrCounts[currChar] == secondStrCounts.get(currChar,0):

				matches += 1

			elif firstStrCounts[currChar] == secondStrCounts.get(currChar,0) - 1:

				matches -= 1

			start += 1

		if matches == 26:

			result.append(start)

		return result
