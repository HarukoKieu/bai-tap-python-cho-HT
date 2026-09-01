"""Tính Tổng Sn = 2 + 4 + 6 + ... + 2n
Input Format
Một số nguyên dương n

Constraints
1 ≤ n ≤ 10⁹
Output Format
In ra giá trị của tổng Sn
"""

n = int(input())
S = n * (n + 1)
print(S)