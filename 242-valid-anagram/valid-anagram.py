class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        for i in s:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1
        for i in t:
            if i not in dic1:
                return False
            else:
                dic1[i] -= 1
        for ch in dic1:
            if dic1[ch] != 0:
                return False
        return True