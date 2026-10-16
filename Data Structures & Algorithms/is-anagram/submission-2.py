class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}

        for ch in s:
            if ch in str1:
                str1[ch] += 1
            else :
                str1[ch] = 1
        for ch in t:
            if ch in str2:
                str2[ch] += 1
            else:
                str2[ch] = 1

        return str1 == str2
        