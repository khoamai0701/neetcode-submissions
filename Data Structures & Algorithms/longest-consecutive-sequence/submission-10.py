class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        count = 1
        numbers = set(nums)

        for num in numbers:
            if num - 1 in numbers:
                continue
            else:
                while num + 1 in numbers:
                    count += 1
                    num += 1
                if count > longest:
                    longest = count
                count = 1

        return longest