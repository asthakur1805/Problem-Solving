class Solution:

	def lengthOfLongestSubstring(self, inputStr):

		inputLength, resultLength = len(inputStr), 0

		charSet = set()

		for startIndex in range(inputLength):

			currLength = 0

			for currIndex in range(startIndex, inputLength):

				if inputStr[currIndex] in charSet:

					charSet.clear()

					break

				else:

					charSet.add(inputStr[currIndex])
					
					currLength += 1

					resultLength = max(resultLength, currLength)


		return resultLength 