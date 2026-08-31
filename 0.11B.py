"""Xây dựng chương trình Python nhập vào một số nguyên dương n. Hãy xử lý và xuất ra màn hình dãy số tự nhiên tăng dần từ 1 sao cho:

Tổng của dãy số vừa lớn hơn n,
Số lượng phần tử trong dãy là ít nhất.
Dữ liệu vào:
Một số nguyên dương n (1 ≤ n ≤ 10⁶)
Dữ liệu ra:
Một dòng duy nhất là dãy số tự nhiên tăng dần từ 1 có tổng lớn hơn n, cách nhau bởi dấu cách.
"""

n = int(input())
s = 0
k = 0
while s <= n:
    k += 1
    s += k
print(*range(1, k + 1))