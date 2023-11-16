from collections import deque

class Solution:

	def eventualSafeNodes(self,graph):

		numberNodes, queue, result = len(graph), deque([]), [] 

		graphRev = [[] for _ in range(numberNodes)]

		indegree = {node:0 for node in range(numberNodes)}

		for currNode in range(numberNodes):

			for neighborNode in graph[currNode]:

				graphRev[neighborNode].append(currNode)
				indegree[currNode] += 1

		for node,degree in indegree.items():

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
		