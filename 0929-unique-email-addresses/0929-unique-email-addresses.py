class Solution:

	def numUniqueEmails(self,inputStrs):

		emailSet = set()

		for currStr in inputStrs:

			local, domain = currStr.split('@')
			local = local.split('+')[0]
			local = local.replace('.','')

			emailSet.add((local,domain))

		return len(emailSet)