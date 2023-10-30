class Solution:

	def eventualSafeNodes(self,graph):

		numberNodes = len(graph)

		visited = [0] * numberNodes

		for startNode in range(numberNodes):

			if visited[startNode] == 0:

				self.dfs(graph,startNode,visited)

		result = []

		for currNode in range(numberNodes):

			if visited[currNode] == 1:

				result.append(currNode)

		return result

	def dfs(self,graph,currNode,visited):

		visited[currNode] = 2

		for neighborNode in graph[currNode]:

			if (visited[neighborNode] == 0 and self.dfs(graph,neighborNode,visited)) or visited[neighborNode] == 2 : 

					return

		visited[currNode] = 1

		return
		

				
		