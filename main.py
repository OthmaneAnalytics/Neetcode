

def hasDuplicate(nums):
    dic = {}
    for item in nums:
        if item in dic.keys():
            return True
        else:
            dic[item] = None
    return False
    
def isAnagram(s , t):
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

def twoSum(nums , target):
    for i in range(len(nums)):
        if target - nums[i] in nums[i+1:]:
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [ i, j]

def char_dic(s):
    d = {}
    for i in s:
        if i in d.keys():
            d[i] +=1
        else:
            d[i] =1
    return d

def compare_s(s_1,s_2):
    d1, d2 = char_dic(s_1), char_dic(s_2)
    if d1.keys() != d2.keys():
        return False
    else:
        for i in d1.keys():
            if d1[i] != d2[i]:
                return False
    return True


def groupAnagrams(strs):
    ana_list = [[strs[0]]]
    for i in range(1,len(strs)):
        has_ana = False
        for j in range(len(ana_list)):
            if compare_s(ana_list[j][0],strs[i]):
                ana_list[j].append(strs[i])
                has_ana = True
        if not has_ana:
            ana_list.append([strs[i]])
            print(ana_list)
    return ana_list

def main():
    print(groupAnagrams (["act","pots","tops","cat","stop","hat"]))


main()
