class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        count = 1
        longest = 0

        for n in numbers:
            if n - 1 in numbers:
                continue
            else: #found start so start counting 
                while n + 1 in numbers:
                    count = count + 1
                    n = n + 1

                if (count > longest):
                    longest = count
                count = 1
        return longest
        
        