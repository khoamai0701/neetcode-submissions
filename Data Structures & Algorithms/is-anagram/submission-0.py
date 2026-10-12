class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        counts2 = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in t:
            counts2[ch] = counts2.get(ch, 0) + 1
        
        return counts == counts2