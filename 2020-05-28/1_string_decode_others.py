"""
参考的别人填写内容
https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/

辅助栈法： 构建辅助栈 stack, 遍历字符串 s 中每个字符 c
- 当 c 为数字时，将数字字符转化为数字 multi，用于后续倍数计算
- 当 c 为字母时，在 res 尾部添加 c
- 当 c 为 [ 时，将当前 multi 和 res 入栈，并分别置0置空
    1. 记录 [ 前的临时结果 res 入栈，是为了用于发现对应 ] 后的拼接操作
    2. 记录 [ 前的倍数 multi 入栈，是为了用于发现对应 ] 后，获取 multi * [...] 字符串
    3. 进入到新 [ 后，res 和 multi 需要重新记录
- 当 c 为 ] 时，stack 出栈，拼接字符串 res = last_res + cur_multi * res
    1. last_res 是上个 [ 到当前 [ 的字符串
    2. cur_multi 是当前 [ 到 ] 内字符串的重复倍数

最后返回字符 res
"""

class Solution:
    def decodeString(self, s: str) -> str:
    stack, res, multi = [], "", 0
    for c in s:
        if c == '[':
            stack.append((multi, res))
            res, multi = '', 0
        elif c == ']':
            cur_multi, last_res = stack.pop()
            res = last_res + cur_multi * res
        elif '0' <= c <= '9':
            multi = multi * 10 + int(c)
        else:
            res += c
    return res


"""
使用正则表达式，比较简洁的版本
参考： https://leetcode-cn.com/problems/decode-string/solution/py3de-5xing-zheng-ze-regex-by-tangchuqi/
"""
class SolutionRe:
    def decodeString(self, s: str) -> str:
        pattern = re.compile(r'(\d+)\[(\w+)\]')
        matchInfo = pattern.findall(s)

        while matchInfo:
            for num, char in matchInfo:
                s = s.replace(f'{num}[{char}]', int(num) * char)
            matchInfo = pattern.findall(s)
        return s
