#
# * 851. 喧闹和富有 - M
# 有一组 n 个人作为实验对象，从 0 到 n - 1 编号，其中每个人都有不同数目的钱，以及不同程度的安静值（quietness）。为了方便起见，我们将编号为 x 的人简称为 "person x "。
# 给你一个数组 richer ，其中 richer[i] = [ai, bi] 表示 person ai 比 person bi 更有钱。另给你一个整数数组 quiet ，其中 quiet[i] 是 person i 的安静值。
# richer 中所给出的数据 逻辑自洽（也就是说，在 person x 比 person y 更有钱的同时，不会出现 person y 比 person x 更有钱的情况 ）。
# 现在，返回一个整数数组 answer 作为答案，其中 answer[x] = y 的前提是，在所有拥有的钱肯定不少于 person x 的人中，person y 是最不安静的人（也就是安静值 quiet[y] 最小的人）。

# 示例 1：
# 输入：richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
# 输出：[5,5,2,5,4,5,6,7]
# 解释：
# answer[0] = 5，
# person 5 比 person 3 有更多的钱，person 3 比 person 1 有更多的钱，person 1 比 person 0 有更多的钱。
# 唯一较为安静（有较低的安静值 quiet[x]）的人是 person 7，
# 但是目前还不清楚他是否比 person 0 更有钱。
# answer[7] = 7，
# 在所有拥有的钱肯定不少于 person 7 的人中（这可能包括 person 3，4，5，6 以及 7），
# 最安静（有较低安静值 quiet[x]）的人是 person 7。
# 其他的答案也可以用类似的推理来解释。
# 示例 2：
# 输入：richer = [], quiet = [0]
# 输出：[0]

# 提示：
# n == quiet.length
# 1 <= n <= 500
# 0 <= quiet[i] < n
# quiet 的所有值 互不相同
# 0 <= richer.length <= n * (n - 1) / 2
# 0 <= ai, bi < n
# ai != bi
# richer 中的所有数对 互不相同
# 对 richer 的观察在逻辑上是一致的

from collections import defaultdict


class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        """拓扑排序 + 递推 (动态规划)"""
        n = len(quiet)
        next_richer = defaultdict(list)
        indegree = [0] * n
        for p1, p2 in richer:
            next_richer[p1].append(p2)
            indegree[p2] += 1

        queue = [i for i in range(n) if indegree[i] == 0]

        ans = [i for i in range(n)]

        while queue:
            cur = queue.pop(0)
            for nxt in next_richer[cur]:
                if quiet[ans[cur]] < quiet[ans[nxt]]:
                    ans[nxt] = ans[cur]
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return ans


if __name__ == "__main__":
    sol = Solution()
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]
    print(sol.loudAndRich(richer, quiet))
