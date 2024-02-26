class Solution:

	def validIPAddress(self,queryIP):

		if '.' in queryIP:

			splitted = queryIP.split('.')

			if len(splitted) != 4:
	
				return 'Neither'

			for part in splitted:

				if len(part) == 0 or (len(part)>1 and part[0]=='0'):

					return 'Neither'

				for char in part:

					if not(ord('0')<=ord(char)<=ord('9')):

						return 'Neither'

				if int(part) > 255:

					return 'Neither'

			return 'IPv4'

		if ':' in queryIP:

			splitted = queryIP.split(':')

			if len(splitted) != 8:

				return 'Neither'

			for part in splitted:

				if len(part) == 0 or len(part) > 4:

					return 'Neither'

				for char in part:

					if not(ord('0')<=ord(char)<=ord('9') or ord('a')<=ord(char)<=ord('f') or ord('A')<=ord(char)<=ord('F')):

						return 'Neither'

			return 'IPv6'

		return 'Neither'

				
			