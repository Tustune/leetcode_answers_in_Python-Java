# 38 count and say 报数

__author__ = "Yang Xuan (jumpthepig@gmail.com)"


import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @classmethod
    @time_it
    def countAndSay(self, n: int) -> str:
        prev_person = '1'
        for i in range(1, n):
            next_person, num, count = '', prev_person[0], 1
            for j in range(1, len(prev_person)):
                if prev_person[j] == num:
                    count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num  # Add last one
            prev_person = next_person
        return prev_person


case1 = 1
assert Solution.countAndSay(case1) == '1'

case2 = 4
assert Solution.countAndSay(case2) == '1211'
