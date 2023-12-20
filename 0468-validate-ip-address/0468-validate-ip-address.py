from re import search

class Solution:

	def validIPAddress(self,queryIP):

		v4Regex = "^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).){4}$"

		v6Regex = "^(([0-9a-fA-F]){1,4}:){8}$"

		if search(v4Regex,queryIP+"."):

			return 'IPv4'

		if search(v6Regex,queryIP+":"):

			return 'IPv6'

		return 'Neither'