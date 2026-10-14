class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if (num in counts):
                counts[num] = counts[num] + 1
            
            else:
                counts[num] = 1
        
        ordered = sorted(counts, key=counts.get, reverse=True)
        return ordered[:k]