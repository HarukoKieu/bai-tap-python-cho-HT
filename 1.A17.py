"""Tính Tổng Các Phần Tử Trong Cấp Số Cộng
Input Format
Một dòng chứa ba số nguyên n, u1, d lần lượt là:

n: Số phần tử của dãy cấp số cộng.
u1: Phần tử đầu tiên.
d: Công sai.
Constraints
2 ≤ n ≤ 10000
1 ≤ u1, d ≤ 10⁶
Output Format
In ra tổng của dãy cấp số cộng gồm n phần tử.

Ví dụ:
Dữ liệu vào:
2 4 7
Dữ liệu ra:
15
Vì dãy là: 4, 11 → Tổng = 15

Công thức:
Sn = n × (2 × u1 + (n − 1) × d) // 2
"""

n, u1, d = map(int, input().split())
print(n * (2 * u1 + (n - 1) * d) // 2)   