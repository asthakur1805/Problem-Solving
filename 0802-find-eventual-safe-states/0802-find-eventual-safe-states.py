class Solution:

	def eventualSafeNodes(self, graph):

		visited = [0]*len(graph)

		for currNode in range(len(graph)):

			if not visited[currNode]:

				self.dfs(graph, currNode, visited)

		result = []

		for currNode in range(len(visited)):

			if visited[currNode] == 1:

				result.append(currNode)

		return result

		
	def dfs(self, graph, currNode, visited):

		visited[currNode] = 2

		for neighborNode in graph[currNode]:

			if not visited[neighborNode]:

				if self.dfs(graph,neighborNode,visited):

					return True

			elif visited[neighborNode] == 2:

				return True

		visited[currNode] = 1
		return

