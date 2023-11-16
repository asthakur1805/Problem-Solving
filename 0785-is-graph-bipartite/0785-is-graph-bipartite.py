class Solution:

	def isBipartite(self,graph):

		numberNodes, visited = len(graph), {}

		for currNode in range(numberNodes):

			if currNode not in visited and not self.dfs(graph,currNode,0,visited):

				return False

		return True

	def dfs(self,graph,currNode,currColor,visited):

		visited[currNode] = currColor

		for neighborNode in graph[currNode]:

			if (neighborNode not in visited and not self.dfs(graph,neighborNode,1-currColor,visited)) or (neighborNode in visited and visited[neighborNode] != 1-currColor):

					return False

		return True

				

				

		

				