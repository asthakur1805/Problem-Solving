class TrieNode:

	def __init__(self):

		self.children = {}
		self.endOfWord = False

class Solution:

	def wordBreak(self,inputStr,wordDict):

		root = TrieNode()

		for word in wordDict:

			curr = root

			for char in word:

				if char not in curr.children:

					curr.children[char] = TrieNode()

				curr = curr.children[char]

			curr.endOfWord = True

		dp = [False]*(len(inputStr)+1)

		dp[len(inputStr)] = True

		for start in range(len(inputStr)-1,-1,-1):

			curr = root

			for end in range(start,len(inputStr)):

				char = inputStr[end]

				if char not in curr.children:

					break

				curr = curr.children[char]

				if curr.endOfWord and dp[end+1]:

					dp[start] = True
					break

		return dp[0]
