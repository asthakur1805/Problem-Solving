from collections import deque

class Solution:

	def isBipartite(self,adjList):

		numberNodes, visited = len(adjList), {}

		for startNode in range(numberNodes):

			if startNode not in visited and not self.bfs(adjList,startNode,visited):

				return False

		return True

	def bfs(self,adjList,startNode,visited):

		currColor = 0

		queue = deque([startNode])
		visited[startNode] = currColor

		while queue:

			currColor = 1 - currColor

			for _ in range(len(queue)):

				currNode = queue.popleft()
				
				for neighborNode in adjList[currNode]:

					if neighborNode not in visited:

						visited[neighborNode] = currColor
						queue.append(neighborNode)

					elif visited[neighborNode] != currColor:

						return False

		return True

						
					

		