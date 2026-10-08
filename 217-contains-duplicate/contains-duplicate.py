class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num = {}
        for i in nums:
            if i not in num:
                num[i] = 1
            else:
                return True
        return False
       