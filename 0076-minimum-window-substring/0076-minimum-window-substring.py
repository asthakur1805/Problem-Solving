class Solution:

	def minWindow(self,firstStr,secondStr):

		countsFirstStr, countsSecondStr =  {}, {}

		for char in secondStr:

			countsSecondStr[char] = countsSecondStr.get(char,0) + 1
			countsFirstStr[char] = 0

		have, need = 0, len(countsSecondStr)

		resultStart, resultEnd, resultLength = 0, -1, float('inf') 

		start = 0

		for end in range(len(firstStr)):

			if firstStr[end] in countsFirstStr:

				countsFirstStr[firstStr[end]] += 1

				if countsFirstStr[firstStr[end]] == countsSecondStr[firstStr[end]]:

					have += 1

			while have >= need:

				if end-start+1 < resultLength:

					resultStart, resultEnd, resultLength = start, end, end-start+1

				if firstStr[start] in countsFirstStr:

					countsFirstStr[firstStr[start]] -= 1

					if countsFirstStr[firstStr[start]] == countsSecondStr[firstStr[start]] - 1:
		
						have -= 1

				start += 1

		return firstStr[resultStart:resultEnd+1]
