"""
内容：给定一个经过编码的字符串，返回它解码后的字符串
环境：python3.6
例子：
s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
"""

import re


class Solution:
    @staticmethod
    def getSubStr(s: str) -> list:
        pattern = r"[0-9]+\[[^0-9\]]+\]"
        result = re.findall(pattern, s)
        return list(set(result))

    @staticmethod
    def replaceSubStr(s: str) -> str:
        pattern = r"^([0-9]+)\[(.*)\]$"
        result = re.findall(pattern, s)
        returnStr = ''
        for i in result:
            returnStr += int(i[0]) * i[1]
        return returnStr

    def decodeString(self, s: str) -> str:
        returnStr = s
        patternStrList = Solution.getSubStr(returnStr)

        while patternStrList:
            patternDict = {i: Solution.replaceSubStr(i) for i in patternStrList}
            for key, value in patternDict.items():
                returnStr = returnStr.replace(key, value)
            patternStrList = Solution.getSubStr(returnStr)
        
        return returnStr


if __name__ == '__main__':
    s = "3[a]2[bc]"
    decodes = Solution().decodeString(s)
    print(f'{s} => {decodes}')
    s = "3[a2[c]]"
    decodes = Solution().decodeString(s)
    print(f'{s} => {decodes}')
    s = "2[abc]3[cd]ef"
    decodes = Solution().decodeString(s)
    print(f'{s} => {decodes}')


