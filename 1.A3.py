"""Tính Giá Trị Biểu Thức Arit
Cho ba số nguyên dương a, b và c, hãy tính giá trị của biểu thức:

S = a × (b + c) + b × (a + c)
Input Format
Một dòng chứa ba số nguyên dương a, b, c cách nhau bởi dấu cách.

Constraints
0 < |a|, |b|, |c| ≤ 10^9
Output Format
Một dòng duy nhất ghi giá trị của biểu thức S.
"""

a, b, c = map(int, input().split())
S = a * (b + c) + b * (a + c)   
print(S)