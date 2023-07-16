from collections import deque

class Solution:

	def isBipartite(self, graph):

		color, visited = {}, set()

		for startNode in range(len(graph)-1):

			if startNode not in visited:

				if not self.bfs(graph, startNode, visited, color):

					return False

		return True

	def bfs(self, graph, startNode, visited, color):

		visited.add(startNode)
		queue, color[startNode],neighborColor = deque([startNode]), 0, 1

		while queue:

			for _ in range(len(queue)):

				currNode = queue.popleft()

				for neighborNode in graph[currNode]:

					if neighborNode not in visited:

						visited.add(neighborNode)
						queue.append(neighborNode)
						color[neighborNode] = neighborColor

					elif color[neighborNode] != neighborColor:

						return False

			neighborColor = 1-neighborColor

		return True

						
					
	

	