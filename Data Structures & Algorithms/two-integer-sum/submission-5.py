class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i, n in enumerate(nums):
            if target - n in sums:
                return list([sums[target - n], i])
            else:
                sums[n] = i