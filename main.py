# Arrays

    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for item in nums:
            if item in dic.keys():
                return True
            else:
                dic[item] = None
        return False
        
         
