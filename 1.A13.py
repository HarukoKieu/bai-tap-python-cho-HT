"""Tìm Số Chia Hết Cho b Nhỏ Nhất Lớn Hơn Hoặc Bằng a
Input Format
Một dòng chứa hai số nguyên dương a và b

Constraints
1 ≤ b ≤ a ≤ 10^8
Output Format
In ra số chia hết cho b nhỏ nhất và ≥ a

Ví dụ
Dữ liệu vào:
21 5
Dữ liệu ra:
25
Vì 25 là số nhỏ nhất ≥ 21 và chia hết cho 5.

Công thức:
result = ((a + b - 1) // b) * b
"""

a, b = map(int, input().split())
print(((a + b - 1) // b) * b)