#!/usr/bin/env python3
from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


if __name__ == '__main__':

    solution = Solution()
    print(solution.longestCommonPrefix(['flower', 'flow', 'flight']))
    print(solution.longestCommonPrefix(['dog', 'racecar', 'car']))
