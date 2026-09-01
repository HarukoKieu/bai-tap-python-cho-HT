"""Đặt Domino Trên Bảng M×N
Mô tả
Bạn có một bảng hình chữ nhật kích thước M × N và số lượng không giới hạn các domino kích thước 2 × 1.

Bạn cần tìm số domino tối đa có thể đặt được trên bảng sao cho:

Mỗi domino chiếm đúng 2 ô vuông đơn vị.
Không có domino nào trùng nhau.
Mỗi domino hoàn toàn nằm trong bảng.
Input Format
Hai số nguyên dương M và N

Constraints
1 ≤ M, N ≤ 10⁹
Output Format
In ra số domino tối đa có thể đặt được.

Ví dụ:
Dữ liệu vào:
6 4
Dữ liệu ra:
12
Công Thức:
Số domino tối đa = (M × N) // 2
Vì mỗi domino chiếm 2 ô đơn vị.
"""

M, N = map(int, input().split())
print((M * N) // 2)