class TrieNode:

	def __init__(self):

		self.children = {}
		self.endOfWord = False

class WordDictionary:

	def __init__(self):

		self.root = TrieNode()

	def addWord(self,word):

		curr = self.root

		for char in word:

			if char not in curr.children:

				curr.children[char] = TrieNode()

			curr = curr.children[char]

		curr.endOfWord = True

	def search(self,word):

		return self.dfs(word,0,self.root)

	def dfs(self,word,startIndex,root):

		curr = root

		for currIndex in range(startIndex,len(word)):

			char = word[currIndex]

			if char == '.':

				for child in curr.children.values():

					if self.dfs(word,currIndex+1,child):

						return True

				return False

			else:

				if char not in curr.children:

					return False

				curr = curr.children[char]

		return curr.endOfWord