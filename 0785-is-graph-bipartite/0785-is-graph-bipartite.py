from collections import deque

class Solution:

	def isBipartite(self, graph):

		colored = {}

		for startNode in range(len(graph)):

			if startNode not in colored:

				if not self.bfs(graph, startNode, colored):

					return False

		return True

	def bfs(self, graph, startNode, colored):

		colored[startNode], neighborColor = 0, 1

		queue = deque([startNode])

		while queue:

			for _ in range(len(queue)):

				currNode = queue.popleft()

				for neighborNode in graph[currNode]:

					if neighborNode not in colored:

						queue.append(neighborNode)
						colored[neighborNode] = neighborColor

					else:

						if colored[neighborNode] != neighborColor:

							return False

			neighborColor = 1 - neighborColor

		return True
		