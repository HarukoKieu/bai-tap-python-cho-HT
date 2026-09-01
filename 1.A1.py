"""Tính Phần Nguyên và Phần Dư của Phép Chia
Input Format
Gồm một dòng chứa 2 số nguyên a và b.

Constraints
b khác 0
1 ≤ a, b ≤ 10^18
Output Format
In ra 1 dòng gồm:

Phần nguyên của phép chia a // b
Phần dư của phép chia a % b Cách nhau bởi dấu cách.
"""

a, b = map(int, input().split())
print(a // b, a % b, sep=" ")