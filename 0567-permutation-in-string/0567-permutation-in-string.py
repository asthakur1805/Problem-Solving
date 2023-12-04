class Solution:

	def checkInclusion(self,firstStr,secondStr):

		if len(firstStr) > len(secondStr): return False

		firstStrCounts, secondStrCounts = [0]*26, [0]*26

		for index in range(len(firstStr)):

			firstStrCounts[ord(firstStr[index])-ord('a')] += 1
			secondStrCounts[ord(secondStr[index])-ord('a')] += 1

		start = 0

		for end in range(len(firstStr),len(secondStr)):

			if self.equals(firstStrCounts,secondStrCounts): return True

			secondStrCounts[ord(secondStr[start])-ord('a')] -= 1
			secondStrCounts[ord(secondStr[end])-ord('a')] += 1

			start += 1

		return self.equals(firstStrCounts,secondStrCounts)

	def equals(self,firstArr,secondArr):

		for firstNum,secondNum in zip(firstArr,secondArr):

			if firstNum != secondNum:

				return False

		return True
			