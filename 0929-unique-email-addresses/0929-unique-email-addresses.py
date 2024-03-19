class Solution:

	def numUniqueEmails(self,emails):

		emailSet = set()

		for email in emails:

			index = 0

			local = ''

			while email[index] not in ('+','@'):

				if email[index] != '.':
					
					local += email[index]

				index += 1

			while email[index] != '@':

				index += 1

			domain = email[index+1:]

			emailSet.add((local,domain))

		return len(emailSet)

		