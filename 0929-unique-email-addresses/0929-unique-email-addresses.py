class Solution:

	def numUniqueEmails(self,inputStrs):

		emailSet = set()

		for currStr in inputStrs:

			local, index = "", 0

			while currStr[index] not in ('+','@'):

				if currStr[index] != '.':
				
					local += currStr[index]

				index += 1

			while currStr[index] != '@':

				index += 1

			index += 1

			domain = ""

			while index < len(currStr):

				domain += currStr[index]
				index += 1

			emailSet.add((local,domain))

		return len(emailSet)