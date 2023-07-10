from collections import deque

class Solution:

	def isBipartite(self, graph):

		colored = {}

		for startNode in range(len(graph)):

			if startNode not in colored:

				if not self.helper(graph, startNode, colored):

					return False

		

		return True

	def helper(self, graph, startNode, colored):

		colored[startNode], currColor, neighborColor = 'A', 'A', 'B'
		queue = deque([startNode])

		while queue:

			for _ in range(len(queue)):

				currNode = queue.popleft()

				for neighborNode in graph[currNode]:

					if neighborNode not in colored:

						queue.append(neighborNode)
						colored[neighborNode] = neighborColor

					else:

						if colored[neighborNode] == currColor:

							return False

			neighborColor, currColor = currColor, neighborColor

		return True