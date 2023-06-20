class Solution:

	def findCircleNum(self, isConnected):

		visited = set()
		count = 0

		for startNode in range(len(isConnected)):

			if startNode not in visited:

				count+=1
				self.dfs(isConnected,startNode,visited)

		return count

	def dfs(self, isConnected, startNode, visited):

		visited.add(startNode)
		
		for otherNode in range(len(isConnected)):

			if isConnected[startNode][otherNode] and otherNode not in visited:

				self.dfs(isConnected, otherNode, visited)



	