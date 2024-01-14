class Solution:

	def findAnagrams(self,firstStr,secondStr):

		if len(secondStr) > len(firstStr):

			return []

		result = []

		countsFirstStr = [0]*26
		countsSecondStr = [0]*26

		for index in range(len(secondStr)):

			countsFirstStr[ord(firstStr[index])-ord('a')] += 1
			countsSecondStr[ord(secondStr[index])-ord('a')] += 1

		start = 0

		for end in range(len(secondStr),len(firstStr)):

			self.checkAnagram(countsFirstStr,countsSecondStr,result,start)
			
			countsFirstStr[ord(firstStr[end])-ord('a')] += 1
			countsFirstStr[ord(firstStr[start])-ord('a')] -= 1

			start += 1

		self.checkAnagram(countsFirstStr,countsSecondStr,result,start)

		return result

	def checkAnagram(self,firstArr,secondArr,result,start):

		for index in range(len(firstArr)):

			if firstArr[index] != secondArr[index]:

				return

		result.append(start)