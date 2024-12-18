# * 402. 移掉 K 位数字
# 给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。

# 示例 1 ：
# 输入：num = "1432219", k = 3
# 输出："1219"
# 解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。
# 示例 2 ：
# 输入：num = "10200", k = 1
# 输出："200"
# 解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
# 示例 3 ：
# 输入：num = "10", k = 2
# 输出："0"
# 解释：从原数字移除所有的数字，剩余为空就是 0 。

# 提示：
# 1 <= k <= num.length <= 105
# num 仅由若干位数字（0 - 9）组成
# 除了 0 本身之外，num 不含任何前导零


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """单调栈；栈底小，栈顶大"""
        stack = []
        cnt = 0
        for i, s in enumerate(num):
            while cnt < k and stack and s < num[stack[-1]]:
                stack.pop()
                cnt += 1
            stack.append(i)
        while cnt < k and stack:
            stack.pop()
            cnt += 1

        ans = "".join([num[i] for i in stack]).lstrip("0")
        return ans if ans else "0"

    def removeKdigits2(self, num: str, k: int) -> str:
        numStack = []

        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack

        # 抹去前导零
        return "".join(finalStack).lstrip("0") or "0"


if __name__ == "__main__":
    s = Solution()
    num = "1432219"
    k = 3
    print(s.removeKdigits(num, k))
