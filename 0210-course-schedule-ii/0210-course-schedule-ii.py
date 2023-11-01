from collections import deque

class Solution:

	def findOrder(self,numCourses,prerequisites):

		adjList, indegree, queue, result = [[] for _ in range(numCourses)], {currNode: 0 for currNode in range(numCourses)}, deque([]), []

		for [firstNode,secondNode] in prerequisites:

			adjList[secondNode].append(firstNode)
			indegree[firstNode] += 1

		for node, degree in indegree.items():

			if degree == 0:

				queue.append(node)

		while queue:

			currNode = queue.popleft()

			result.append(currNode)

			for neighborNode in adjList[currNode]:

				indegree[neighborNode] -= 1

				if indegree[neighborNode] == 0:

					queue.append(neighborNode)

		return result if len(result) == numCourses else []

		

			