# Arrays

    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for item in nums:
            if item in dic.keys():
                return True
            else:
                dic[item] = None
        return False
        
 class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for c_s in s:
            if c_s in dic.keys():
                dic[c_s] += 1
            else:
                dic[c_s] = 1
        print(s)
        print(dic)
        for c_t in t:
            if c_t in dic.keys():
                dic[c_t] -= 1
            else:
                return False
        print(dic)
        for index in dic:
            if dic[index] != 0:
                return False
        return True

