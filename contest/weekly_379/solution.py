from functools import cache
from typing import List


class Solution:
    # https://leetcode.com/contest/weekly-contest-379/problems/maximum-area-of-longest-diagonal-rectangle/
    # 3000. Maximum Area of Longest Diagonal Rectangle
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # max_diagonal_square = 0
        # area = 0

        # for x, y in dimensions:
        #     diagonal_square = x**2 + y**2
        #     if diagonal_square > max_diagonal_square or (
        #         diagonal_square == max_diagonal_square and x * y > area
        #     ):
        #         max_diagonal_square = diagonal_square
        #         area = x * y

        # return area

        return max((x**2 + y**2, x * y) for x, y in dimensions)[1]

    def invoke_areaOfMaxDiagonal(self):
        dimensions = [[9, 3], [8, 6]]
        result = self.areaOfMaxDiagonal(dimensions)
        print(result)

    # https://leetcode.com/contest/weekly-contest-379/problems/minimum-moves-to-capture-the-queen/
    # 3001. Minimum Moves to Capture The Queen
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        def not_inside(left: int, mid: int, right: int) -> bool:
            return not min(left, right) < mid < max(left, right)

        if (
            a == e
            and (c != e or not_inside(b, f, d))
            or b == f
            and (d != f or not_inside(a, e, c))
            or c + d == e + f
            and (a + b != e + f or not_inside(c, a, e))
            or c - d == e - f
            and (a - b != e - f or not_inside(c, a, e))
        ):
            return 1

        return 2

    def invoke_minMovesToCaptureTheQueen(self):
        a = 5
        b = 3
        c = 3
        d = 4
        e = 5
        f = 2
        result = self.minMovesToCaptureTheQueen(a, b, c, d, e, f)
        print(result)
        assert result == 1

    # https://leetcode.com/contest/weekly-contest-379/problems/maximum-size-of-a-set-after-removals/
    # 3002. Maximum Size of a Set After Removals
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        common = len(set1 & set2)

        n1 = len(set1)
        n2 = len(set2)
        ans = n1 + n2 - common

        m = len(nums1) // 2
        if n1 > m:
            mn = min(n1 - m, common)
            n1 -= mn
            common -= mn
            ans -= n1 - m
        if n2 > m:
            mn = min(n2 - m, common)
            n2 -= mn
            common -= mn
            ans -= n2 - m

        return ans

    def invoke_maximumSetSize(self):
        nums1 = [1, 2, 3, 4, 5, 6]
        nums2 = [2, 3, 2, 3, 2, 3]
        result = self.maximumSetSize(nums1, nums2)
        print(result)
        assert result == 5

    # https://leetcode.com/contest/weekly-contest-379/problems/maximize-the-number-of-partitions-after-operations/
    # 3003. Maximize the Number of Partitions After Operations
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dfs(i: int, mask: int, changed: bool) -> int:
            if i == len(s):
                return 1

            bit = 1 << (ord(s[i]) - ord("a"))
            new_mask = mask | bit
            if new_mask.bit_count() > k:
                res = dfs(i + 1, bit, changed) + 1
            else:
                res = dfs(i + 1, new_mask, changed)
            if changed:
                return res

            for j in range(26):
                new_mask = mask | (1 << j)
                if new_mask.bit_count() > k:
                    res = max(res, dfs(i + 1, 1 << j, True) + 1)
                else:
                    res = max(res, dfs(i + 1, new_mask, True))
            return res

        return dfs(0, 0, False)

    def invoke_maxPartitionsAfterOperations(self):
        s = "accca"
        k = 2
        result = self.maxPartitionsAfterOperations(s, k)
        print(result)
        assert result == 3


if __name__ == "__main__":
    solution = Solution()
    solution.invoke_areaOfMaxDiagonal()
    solution.invoke_minMovesToCaptureTheQueen()
    solution.invoke_maximumSetSize()
    solution.invoke_maxPartitionsAfterOperations()
