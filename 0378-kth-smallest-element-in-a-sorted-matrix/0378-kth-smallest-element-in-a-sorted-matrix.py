class Solution:

	def kthSmallest(self,matrix,K):

		left, right, result = matrix[0][0], matrix[len(matrix)-1][len(matrix)-1], None

		while left <= right:

			mid = left + (right - left) // 2

			if self.countLessOrEqual(matrix,mid) >= K:

				result = mid
				right = mid - 1

			else:

				left = mid + 1

		return result

	def countLessOrEqual(self,matrix,inputVal):

		count = 0

		for currRow in range(len(matrix)):

			currColumn = -1

			while currColumn < len(matrix)-1 and matrix[currRow][currColumn+1] <= inputVal:

				currColumn += 1

			count += (currColumn+1)

		return count
	

		

		