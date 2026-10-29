class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = 0
        counts = {}
        l = 0
    #xyxy k = 2
        for r in range(len(s)):
            if s[r] in counts:
                counts[s[r]] += 1
                
            else : 
                counts[s[r]] = 1
            top = max(counts.values()) 
            
            while r - l - top + 1 > k:
                counts[s[l]] -= 1
                l += 1
            window = max(window, r - l + 1)
        return window