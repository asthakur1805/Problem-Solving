from collections import deque

class Solution:

	def findOrder(self,numCourses,prerequisites):

		adjList = [[] for _ in range(numCourses)]

		indegree = {course:0 for course in range(numCourses)}

		queue = deque([])

		topoResult = []

		for [secondCourse,firstCourse] in prerequisites:

			adjList[firstCourse].append(secondCourse)

			indegree[secondCourse] += 1

		for node,degree in indegree.items():

			if degree == 0:

				queue.append(node)

		while queue:

			currNode = queue.popleft()

			topoResult.append(currNode)

			for neighborNode in adjList[currNode]:

				indegree[neighborNode] -= 1

				if indegree[neighborNode] == 0:

					queue.append(neighborNode)

		return topoResult if len(topoResult) == numCourses else []