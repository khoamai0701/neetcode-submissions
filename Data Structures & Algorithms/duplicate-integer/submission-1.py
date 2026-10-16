class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        group = set()
        count = 0;

        for n in nums:
            if (n in group):
                return True
            group.add(n)
        
        return False
