class Solution:

	def kClosest(self, points, K):

		dataPoints = [([x,y],x**2+y**2) for [x,y] in points]

		dataPoints.sort(key=lambda data:data[1])

		return [dataPoints[index][0] for index in range(K)]

		