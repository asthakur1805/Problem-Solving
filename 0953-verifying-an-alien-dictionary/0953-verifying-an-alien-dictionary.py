class Solution:

	def isAlienSorted(self,words,order):

		mapping = {char:index for index,char in enumerate(order)}

		for wordIndex in range(len(words)-1):

			firstWord, secondWord = words[wordIndex], words[wordIndex+1]

			for charIndex in range(min(len(firstWord),len(secondWord))):

				if mapping[firstWord[charIndex]] > mapping[secondWord[charIndex]]:

					return False

				elif mapping[firstWord[charIndex]] < mapping[secondWord[charIndex]]:

					break

			else:

				if len(firstWord) > len(secondWord):

					return False

		return True