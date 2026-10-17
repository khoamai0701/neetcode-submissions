class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        group = {}
        s = []
        for i, num  in enumerate(nums):
            if target - num in group:
                
                return sorted([group[target - num], i])
                
            else:
                group[num] = i

        return s
            

