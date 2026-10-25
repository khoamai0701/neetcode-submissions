class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and not lower[l].isalnum():
                l += 1
            while l < r and not lower[r].isalnum():
                r -= 1
            
            if lower[l] != lower[r]:
                return False
            l += 1
            r -= 1
        
        return True

        