'''
249. Group Shifted Strings
Medium

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''

## RC ##
##Python Group by "relative distance"
## APPROACH : GREEDY ##
## LOGIC ##
## 1. Intuition is: there will be some common relative distance among neighbouring
# strings in a given list
## 2.That  difference in ascii values
## 3. Store ascii value pairs in hashmap and group them together.
## 4. To handle rotation  :  If the diff in ascii become -ve then add 26
##  case : acz (2, 23), dfc (2, -3) ==> (2, -3+26 = 23) => can be clubbed together.

## TIME COMPLEXITY : O(N) ##
## SPACE COMPLEXITY : O(N) ##

class Solution:
    def groupStrings(self, strings):
        from collections import defaultdict
        res=defaultdict(list)
        #reldist
        for subString in strings:
            reldist=""
            for ch in range(1,len(subString)):
                reldist+=str((ord(subString[ch]) - ord(subString[ch - 1]) + 26) % 26)
            res[reldist].append(subString)
        return res.values()

S = Solution()
strings=["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
res=S.groupStrings(strings)
print(res)
