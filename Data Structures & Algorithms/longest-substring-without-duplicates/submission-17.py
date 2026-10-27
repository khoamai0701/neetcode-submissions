class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = 1
        count = 0
        
        if len(s) == 0:
            return 0
        
        seen.add(s[l])
        count += 1
        longest = 1
        #abcb
        while r < len(s):
            
            while r < len(s) and not s[r] in seen:
                seen.add(s[r])
                count += 1
                r += 1
            if count > longest:
                longest = count
            while r < len(s) and s[r] in seen:
                seen.remove(s[l])
                l += 1
                count -= 1
                
        return longest
        