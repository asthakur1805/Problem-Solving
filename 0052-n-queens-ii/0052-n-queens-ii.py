class Solution:

	def totalNQueens(self,N):

		colSet, posDiagSet, negDiagSet = set(), set(), set()

		self.count = 0

		self.helper(0,N,colSet,posDiagSet,negDiagSet)

		return self.count

	def helper(self,row,N,colSet,posDiagSet,negDiagSet):

		if row == N:

			self.count += 1

			return

		for column in range(N):

			if column in colSet or row+column in posDiagSet or row-column in negDiagSet:

				continue

			colSet.add(column)
			posDiagSet.add(row+column)
			negDiagSet.add(row-column)
	
			self.helper(row+1,N,colSet,posDiagSet,negDiagSet)

			colSet.remove(column)
			posDiagSet.remove(row+column)
			negDiagSet.remove(row-column)

	

		