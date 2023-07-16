class Solution:

	def isBipartite(self, graph):

		colored, visited = {}, set()

		for startNode in range(len(graph)-1):

			if startNode not in visited:

				if not self.dfs(graph,startNode,colored,visited,0):

					return False

		return True

	def dfs(self,graph,startNode,colored,visited,currColor):

		visited.add(startNode)
		colored[startNode]=currColor

		for neighborNode in graph[startNode]:

			if neighborNode not in visited:

				if not self.dfs(graph,neighborNode,colored,visited,1-currColor):

					return False

			elif colored[neighborNode] == currColor:

					return False

		return True