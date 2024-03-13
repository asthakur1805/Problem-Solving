class Solution:

	def subdomainVisits(self,inputDomains):

		counts = {}

		for cpDomain in inputDomains:

			count, currDomain = cpDomain.split(' ')

			counts[currDomain] = counts.get(currDomain,0) + int(count)

			for subDomainIndex in range(len(currDomain)):

				if currDomain[subDomainIndex] == '.':

					subDomain = currDomain[subDomainIndex+1:]

					counts[subDomain] = counts.get(subDomain,0) + int(count)

		return [f'{count} {subDomain}' for subDomain,count in counts.items()]

			