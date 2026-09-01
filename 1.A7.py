"""Tính Tổng Sn = 1 + 2 + 3 + ... + n
Input Format
Một dòng chứa số nguyên không âm n.

Constraints
0 ≤ n ≤ 10^8
Output Format
In ra tổng Sn = 1 + 2 + 3 + ... + n.
"""

n = int(input())
S = n * (n + 1) // 2
print(S)