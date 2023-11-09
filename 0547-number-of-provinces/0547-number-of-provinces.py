from collections import deque

class Solution:

	def findCircleNum(self,isConnected):

		result, visited = 0, set({})

		for startNode in range(len(isConnected)):

			if startNode not in visited:

				result += 1

				self.bfs(isConnected,startNode,visited)

		return result

	def bfs(self,isConnected,startNode,visited):

		queue = deque([startNode])
		visited.add(startNode)

		while queue:

			currNode = queue.popleft()

			for neighborNode in range(len(isConnected)):

				if neighborNode not in visited and isConnected[currNode][neighborNode]:

					visited.add(neighborNode)
					queue.append(neighborNode)
			