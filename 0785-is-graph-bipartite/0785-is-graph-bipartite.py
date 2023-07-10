class Solution:

	def isBipartite(self, graph):

		colored = {}

		for startNode in range(len(graph)):

			if startNode not in colored:

				if not self.dfs(graph, startNode, colored, 0):

					return False

		return True

	def dfs(self, graph, currNode, colored, currColor):

		colored[currNode] = currColor

		for neighborNode in graph[currNode]:

			if neighborNode not in colored:

				if not self.dfs(graph, neighborNode, colored, 1-currColor):

					return False

			else:

				if colored[neighborNode] != 1 - currColor:

					return False

		return True

		

		

				