class Solution:

	def singleNumber(self, nums):

		result = 0

		for bitPosition in range(32):

			mask = (1 << bitPosition)

			countSetBits = 0

			for num in nums:

				if num & mask:

					countSetBits += 1

			if countSetBits % 3:

				if result + mask >= (1 << 31):

					result += mask - (1 << 32)

				else:

					result += mask

		return result