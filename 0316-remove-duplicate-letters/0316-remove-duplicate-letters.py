class Solution:

	def removeDuplicateLetters(self,inputStr):

		visited = set()
		lastOccur = {}
		stack = []

		for index, char in enumerate(inputStr):

			lastOccur[char] = index


		for index, char in enumerate(inputStr):

			if char not in visited:

				while stack and stack[-1] > char and lastOccur[stack[-1]] > index:

					visited.remove(stack.pop())

				visited.add(char)
				stack.append(char)

		return ''.join(stack)