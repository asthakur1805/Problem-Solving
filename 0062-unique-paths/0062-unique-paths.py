class Solution:

	def uniquePaths(self,numRows,numColumns):

		prev = [0]*numColumns

		for currRow in range(numRows-1,-1,-1):

			curr = [0]*numColumns

			for currColumn in range(numColumns-1,-1,-1):

				if (currRow,currColumn) == (numRows-1,numColumns-1):

					curr[currColumn] = 1

				else:

					right = curr[currColumn+1] if currColumn < numColumns-1 else 0
					down = prev[currColumn] if currRow < numRows-1 else 0

					curr[currColumn] = right+down

			prev = curr

		return prev[0]

					

					
