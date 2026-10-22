class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        count = 1
        numbers = set(nums)
        #[0,3,7,2,5,8,4,6,0,1]
        for n in nums:
            if n - 1 in numbers:
                continue
            
            while n + 1 in numbers:
                count += 1
                n += 1
            if count > longest:
                longest = count
            count = 1
        return longest


