class Solution:

	def validIPAddress(self,queryIP):

		if '.' in queryIP:

			splitted = queryIP.split('.')

			if len(splitted) != 4: return 'Neither'

			allowedSymbols = set(str(num) for num in range(10))

			for part in splitted:

				if len(part) == 0 or (len(part)>1 and part[0]=='0'): return 'Neither'

				for char in part:

					if char not in allowedSymbols: return 'Neither'

				if int(part) > 255: return 'Neither'

			return 'IPv4'

		elif ':' in queryIP:

			splitted = queryIP.split(':')

			if len(splitted) != 8: return 'Neither'

			allowedSymbols = set({'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F'})

			for part in splitted:

				if len(part) == 0 or len(part) > 4: return 'Neither'

				for char in part:

					if char not in allowedSymbols: return 'Neither'

			return 'IPv6'

		return 'Neither'