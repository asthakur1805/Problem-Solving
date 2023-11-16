from collections import deque

class Solution:

	def isBipartite(self,graph):

		numberNodes, visited = len(graph), {}

		for startNode in range(numberNodes):

			if startNode not in visited and not self.bfs(graph,startNode,visited):

				return False

		return True

	def bfs(self,graph,startNode,visited):

		queue, currColor = deque([startNode]), 0
		visited[startNode] = currColor

		while queue:

			currColor = 1-currColor

			for _ in range(len(queue)):

				currNode = queue.popleft()

				for neighborNode in graph[currNode]:

					if neighborNode in visited:

						if visited[neighborNode] != currColor:

							return False

					else:

						queue.append(neighborNode)
						visited[neighborNode] = currColor

		return True