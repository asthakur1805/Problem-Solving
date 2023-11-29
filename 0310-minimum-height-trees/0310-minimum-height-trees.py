from collections import deque

class Solution:

	def findMinHeightTrees(self,numberNodes,edges):

		if numberNodes <= 2:

			return [node for node in range(numberNodes)]

		adjList = [[] for _ in range(numberNodes)]
		degree = {node:0 for node in range(numberNodes)}

		queue = deque([])

		for [firstNode,secondNode] in edges:

			adjList[firstNode].append(secondNode)
			adjList[secondNode].append(firstNode)

			degree[firstNode] += 1
			degree[secondNode] += 1

		for node, currDegree in degree.items():

			if currDegree == 1:

				queue.append(node)

		while numberNodes > 2:

			numberNodes -= len(queue)

			for _ in range(len(queue)):

				currNode = queue.popleft()

				for neighborNode in adjList[currNode]:
	
					degree[neighborNode] -= 1

					if degree[neighborNode] == 1:

						queue.append(neighborNode)

		return [node for node in queue]

		