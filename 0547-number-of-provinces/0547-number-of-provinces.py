from collections import deque

class Solution:

	def findCircleNum(self, isConnected):

		visited = set()
		count = 0

		for startNode in range(len(isConnected)):

			if startNode not in visited:
				
				count += 1
				self.bfs(isConnected, startNode, visited)

		return count

	def bfs(self, isConnected, startNode, visited):

		visited.add(startNode)
		queue = deque([startNode])

		while queue:

			for _ in range(len(queue)):

				currNode = queue.popleft()

				for otherNode in range(len(isConnected)):

					if isConnected[currNode][otherNode] and otherNode not in visited:

						queue.append(otherNode)
						visited.add(otherNode)