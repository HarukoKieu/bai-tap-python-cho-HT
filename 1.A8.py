"""Tính Tổng Bình Phương Sn = 1² + 2² + 3² + ... + n²
Input Format
Một dòng chứa số nguyên không âm n.

Constraints
0 ≤ n ≤ 10^6
Output Format
In ra tổng bình phương Sn.
"""

n = int(input())
S = n * (n + 1) * (2 * n + 1) // 6
print(S)