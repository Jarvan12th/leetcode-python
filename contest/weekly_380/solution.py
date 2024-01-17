from bisect import bisect_left
from functools import cache
from typing import List


class Solution:
    # https://leetcode.com/contest/weekly-contest-380/problems/count-elements-with-maximum-frequency/
    # 3005. Count Elements With Maximum Frequency
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        max_freq = ans = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > max_freq:
                max_freq = ans = freq[num]
            elif freq[num] == max_freq:
                ans += freq[num]

        return ans

    def invoke_maxFrequencyElements(self):
        nums = [1, 2, 2, 3, 1, 4]
        result = self.maxFrequencyElements(nums)
        print(result)
        assert result == 4

    # https://leetcode.com/contest/weekly-contest-380/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/
    # 3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K
    def findMaximumNumber(self, k: int, x: int) -> int:
        left = 0
        right = (k + 1) << x
        while left + 1 < right:
            mid = (left + right) >> 1
            if self.countDigitOne(mid, x) <= k:
                left = mid
            else:
                right = mid
        return left

    # # Binary search + DP
    # def countDigitOne(self, n: int, x: int) -> int:
    #     s = bin(n)[2:]

    #     @cache
    #     def dfs(i: int, cnt: int, is_limit: bool) -> int:
    #         if i == len(s):
    #             return cnt

    #         res = 0
    #         up = int(s[i]) if is_limit else 1
    #         for j in range(up + 1):
    #             res += dfs(
    #                 i + 1,
    #                 cnt + (j == 1 and (len(s) - i) % x == 0),
    #                 is_limit and j == up,
    #             )
    #         return res

    #     return dfs(0, 0, True)

    # Binary search + Enum
    def countDigitOne(self, num: int, x: int) -> int:
        res = 0
        shift = x - 1
        n = num >> shift
        while n:
            res += (n // 2) << shift
            if n % 2:
                mask = (1 << shift) - 1
                res += (num & mask) + 1
            shift += x
            n >>= x
        return res

    def invoke_findMaximumNumber(self):
        k = 7
        x = 2
        result = self.findMaximumNumber(k, x)
        print(result)
        assert result == 9

    # https://leetcode.com/contest/weekly-contest-380/problems/find-beautiful-indices-in-the-given-array-i/
    # https://leetcode.com/contest/weekly-contest-380/problems/find-beautiful-indices-in-the-given-array-ii/
    # 3008. Find Beautiful Indices in the Given Array II
    # # Binary search + KMP
    # def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
    #     pos_a = self.kmp(s, a)
    #     pos_b = self.kmp(s, b)
    #     m = len(pos_b)

    #     ans = []
    #     for i in pos_a:
    #         idx = bisect_left(pos_b, i)
    #         if idx < m and pos_b[idx] - i <= k or idx > 0 and i - pos_b[idx - 1] <= k:
    #             ans.append(i)
    #     return ans

    # Two pointers + KMP
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        pos_a = self.kmp(s, a)
        pos_b = self.kmp(s, b)
        m = len(pos_b)

        ans = []
        idx = 0
        for i in pos_a:
            while idx < m and pos_b[idx] < i - k:
                idx += 1
            if idx < m and abs(pos_b[idx] - i) <= k:
                ans.append(i)
        return ans

    def kmp(self, text: str, pattern: str) -> List[int]:
        m = len(pattern)
        pi = [0] * m
        c = 0
        for i in range(1, m):
            while c and pattern[i] != pattern[c]:
                c = pi[c - 1]
            if pattern[i] == pattern[c]:
                c += 1
            pi[i] = c

        res = []
        c = 0
        for i, v in enumerate(text):
            while c and v != pattern[c]:
                c = pi[c - 1]
            if v == pattern[c]:
                c += 1
            if c == m:
                res.append(i - m + 1)
                c = pi[c - 1]

        return res

    def invoke_beautifulIndices(self):
        s = "isawsquirrelnearmysquirrelhouseohmy"
        a = "my"
        b = "squirrel"
        k = 15
        result = self.beautifulIndices(s, a, b, k)
        print(result)
        assert result == [16, 33]


if __name__ == "__main__":
    solution = Solution()
    # solution.invoke_maxFrequencyElements()
    # solution.invoke_findMaximumNumber()
    solution.invoke_beautifulIndices()
