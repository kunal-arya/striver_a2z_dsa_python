# LINK: https://leetcode.com/problems/longest-common-prefix/

from typing import List



# Brute Force
def largestCommonPrefix(strs: List[str]) -> str:
    minL = len(min(strs))
    ans = ""

    for i in range(minL):
        ch = strs[0][i]
        cnt = 0

        for str in strs:
            if ch == str[i]:
                cnt += 1
        
        if cnt == len(strs):
            ans += ch
        else:
            break
    
    return ans

print(largestCommonPrefix(["flower","flow","flight"]))


