"""Tính Chu Vi và Diện Tích Hình Tròn
Input Format
Một dòng chứa bán kính r là một số nguyên.

Constraints
1 ≤ r ≤ 10^6
Output Format
In ra 2 giá trị:

Chu vi hình tròn
Diện tích hình tròn Cách nhau một khoảng trắng và làm tròn đến 2 chữ số sau dấu thập phân.
Ghi chú: Lấy π ≈ 3.14"""


r = int(input())
pi = 3.14
chu_vi = 2 * pi * r
dien_tich = pi * r ** 2
print(f"{chu_vi:.2f} {dien_tich:.2f}")
