from collections import deque

class Solution:

	def canFinish(self,numCourses,prerequisites):

		adjList = [[] for _ in range(numCourses)]

		indegree = {course:0 for course in range(numCourses)}

		queue = deque([])

		for [secondCourse,firstCourse] in prerequisites:

			adjList[firstCourse].append(secondCourse)

			indegree[secondCourse] += 1

		for node,degree in indegree.items():

			if degree == 0:

				queue.append(node)

		topoResult = []

		while queue:

			currNode = queue.popleft()

			topoResult.append(currNode)

			for neighborNode in adjList[currNode]:

				indegree[neighborNode] -= 1

				if indegree[neighborNode] == 0:

					queue.append(neighborNode)

		return len(topoResult) == numCourses