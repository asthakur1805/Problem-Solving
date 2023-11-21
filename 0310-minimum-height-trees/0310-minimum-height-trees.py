from collections import deque

class Solution:

	def findMinHeightTrees(self,numberNodes,edges):

		if numberNodes == 0:

			return []

		if numberNodes <= 2:

			return [currNode for currNode in range(numberNodes)]

		adjList = [[] for _ in range(numberNodes)]

		queue = deque([])

		degree = {currNode:0 for currNode in range(numberNodes)}

		for [firstNode,secondNode] in edges:

			adjList[firstNode].append(secondNode)
			adjList[secondNode].append(firstNode)

			degree[firstNode] += 1
			degree[secondNode] += 1

		for currNode,currDegree in degree.items():

			if currDegree == 1:

				queue.append(currNode)

		while numberNodes > 2:

			numberNodes -= len(queue)

			for _ in range(len(queue)):

				currNode = queue.popleft()

				for neighborNode in adjList[currNode]:

					degree[neighborNode] -= 1

					if degree[neighborNode] == 1:

						queue.append(neighborNode)

		result = []

		for node in queue:

			result.append(node)

		return result
		