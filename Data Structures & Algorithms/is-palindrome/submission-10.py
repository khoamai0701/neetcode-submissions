class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = s.lower()
        l = 0
        r = len(low) - 1

        while l < r:
            while not low[l].isalnum() and l < r:
                l += 1
            while not low[r].isalnum() and l < r:
                r -= 1
            
            if (low[l] != low[r]):
                return False
            r -= 1
            l += 1
        return True
            



