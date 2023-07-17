from collections import deque

class Solution:

	def eventualSafeNodes(self, graph):

		graphRev = [[] for _ in range(len(graph))]

		indegree = {node:0 for node in range(len(graph))}

		for currNode in range(len(graph)):

			for neighborNode in graph[currNode]:

				graphRev[neighborNode].append(currNode)
				indegree[currNode] += 1

		queue, result = deque([]), []

		for currNode, degree in indegree.items():

			if degree == 0:

				queue.append(currNode)
		
		while queue:

			currNode = queue.popleft()

			result.append(currNode)

			for neighborNode in graphRev[currNode]:

				indegree[neighborNode] -= 1

				if indegree[neighborNode] == 0:

					queue.append(neighborNode)

		result.sort()

		return result