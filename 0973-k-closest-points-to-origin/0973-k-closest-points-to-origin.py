class Solution:

	def kClosest(self,points,K):

		if K >= len(points):

			return points

		return self.quickSelect(points,K,0,len(points)-1)

	def quickSelect(self,points,K,left,pivot):

		mid = left + (pivot - left) // 2

		points[mid], points[pivot] = points[pivot], points[mid]

		partition = left

		pivotDistance = self.calculateDistance(points[pivot])

		for curr in range(left,pivot):

			if self.calculateDistance(points[curr]) <= pivotDistance:

				points[partition], points[curr] = points[curr], points[partition]
				partition += 1

		points[partition], points[pivot] = points[pivot], points[partition]

		if K == partition:

			return points[:K]

		return self.quickSelect(points,K,left,partition-1) if K < partition else self.quickSelect(points,K,partition+1,pivot)

	def calculateDistance(self,point):

		return point[0]**2 + point[1]**2



			



		
		

		