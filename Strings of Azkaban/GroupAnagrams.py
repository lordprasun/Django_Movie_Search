"""
Given an array of strings, group anagrams together.
"""
from collections import defaultdict

def groupAnagrams_1(strs):
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

def groupAnagrams_2(strs):
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


if __name__=='__main__':
    result = groupAnagrams_1(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)