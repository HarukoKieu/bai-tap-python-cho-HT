"""Tìm Số Chia Hết Cho b Lớn Nhất Không Vượt Quá a
Input Format
Một dòng chứa hai số nguyên dương a và b

Constraints
1 ≤ b ≤ a ≤ 10^8
Output Format
In ra số lớn nhất không vượt quá a và chia hết cho b
"""

a, b = map(int, input().split())
print(a // b * b)