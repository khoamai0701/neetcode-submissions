class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        count = 1
        longest = 0

        for n in nums:
            if n - 1 in numbers:
                continue;
            while n + 1 in numbers:
                count += 1
                n += 1
            if count > longest:
                longest = count
            count = 1

            
        return longest