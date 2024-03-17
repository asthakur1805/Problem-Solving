class TrieNode:

	def __init__(self):

		self.children = {}
		self.endOfWord = False

class Solution:

	def findWords(self,board,words):

		root, visited, builder, directions = TrieNode(), set(), [], [(-1,0),(1,0),(0,-1),(0,1)]

		numRows, numColumns = len(board), len(board[0])

		result = []

		for word in words:

			self.addWord(root,word)

		for startRow in range(numRows):

			for startColumn in range(numColumns):

				self.dfs(board,startRow,startColumn,root,builder,numRows,numColumns,visited,directions,result)

		return result

	def dfs(self,board,currRow,currColumn,curr,builder,numRows,numColumns,visited,directions,result):

		if curr.endOfWord:

			result.append(''.join(builder))
			curr.endOfWord = False

		if not(0 <= currRow < numRows) or not(0 <= currColumn < numColumns) or (currRow,currColumn) in visited or board[currRow][currColumn] not in curr.children:

			return

		builder.append(board[currRow][currColumn])
		visited.add((currRow,currColumn))
		curr = curr.children[board[currRow][currColumn]]

		for rowDirection,columnDirection in directions:

			self.dfs(board,currRow+rowDirection,currColumn+columnDirection,curr,builder,numRows,numColumns,visited,directions,result)

		visited.remove((currRow,currColumn))
		builder.pop()

	def addWord(self,root,word):

		curr = root

		for currChar in word:

			if currChar not in curr.children:

				curr.children[currChar] = TrieNode()

			curr = curr.children[currChar]

		curr.endOfWord = True
