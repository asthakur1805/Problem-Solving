from collections import deque

class Solution:

	def findOrder(self, numCourses, prerequisites):

		adjList = [[] for _ in range(numCourses)]
		indegree = {course:0 for course in range(numCourses)}

		for [currCourse, prerequisiteCourse] in prerequisites:

			adjList[prerequisiteCourse].append(currCourse)
			indegree[currCourse]+=1

		result, queue = [], deque([])

		for currCourse in range(numCourses):
				
			if indegree[currCourse] == 0:

				queue.append(currCourse)

		while queue:

			prerequisiteCourse = queue.popleft()

			result.append(prerequisiteCourse)

			for currCourse in adjList[prerequisiteCourse]:

				indegree[currCourse] -= 1

				if indegree[currCourse] == 0:

					queue.append(currCourse)

		return result if len(result) == numCourses else []