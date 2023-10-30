class Solution:

	def isBipartite(self,graph):

		numberNodes, visited = len(graph), {}

		for startNode in range(numberNodes):

			if startNode not in visited and not self.dfs(graph,startNode,visited,0):

				return False

		return True

	def dfs(self,graph,currNode,visited,currColor):

		visited[currNode] = currColor
		
		for neighborNode in graph[currNode]:

			if (neighborNode not in visited and not self.dfs(graph,neighborNode,visited,1-currColor)) or (neighborNode in visited and visited[neighborNode] == currColor):

					return False

		return True
						
					

		