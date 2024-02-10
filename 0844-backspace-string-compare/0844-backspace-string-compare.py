class Solution:

	def backspaceCompare(self,firstStr,secondStr):

		firstStrIndex, secondStrIndex = len(firstStr)-1, len(secondStr)-1

		while firstStrIndex >= 0 or secondStrIndex >= 0:

			firstStrIndex = self.getNextValidChar(firstStr,firstStrIndex)
			secondStrIndex = self.getNextValidChar(secondStr,secondStrIndex)
			
			firstChar =  firstStr[firstStrIndex] if firstStrIndex >= 0 else ''
			secondChar = secondStr[secondStrIndex] if secondStrIndex >= 0 else ''
			
			if firstChar != secondChar:

				return False

			firstStrIndex = firstStrIndex-1 if firstStrIndex >= 0 else firstStrIndex
			secondStrIndex = secondStrIndex-1 if secondStrIndex >= 0 else secondStrIndex

		return True

	def getNextValidChar(self,inputStr,index):

		countBackspaces = 0

		while index >= 0:

			if countBackspaces == 0 and inputStr[index] != '#':

				break

			elif inputStr[index] == '#':

				countBackspaces += 1

			else:

				countBackspaces -= 1

			index -= 1

		return index