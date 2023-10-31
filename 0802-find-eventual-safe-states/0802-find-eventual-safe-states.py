from collections import deque

class Solution:

	def eventualSafeNodes(self,graph):

		numberNodes = len(graph)
		queue, result, indegree = deque([]), [], {currNode: 0 for currNode in range(numberNodes)}

		graphRev = [[] for _ in range(numberNodes)]

		for currNode in range(numberNodes):

			for neighborNode in graph[currNode]:

				graphRev[neighborNode].append(currNode)
				indegree[currNode] += 1

		for node, degree in indegree.items():

			if degree == 0:

				queue.append(node)

		while queue:

			currNode = queue.popleft()

			result.append(currNode)

			for neighborNode in graphRev[currNode]:

				indegree[neighborNode] -= 1

				if indegree[neighborNode] == 0:

					queue.append(neighborNode)

		
		result.sort()

		return result
		

		

		