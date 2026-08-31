"""
Viết chương trình nhập vào:

Số nguyên dương n là số bài kiểm tra đã làm.
n số nguyên tiếp theo là điểm số tương ứng của em.
Hãy:

Sắp xếp danh sách điểm số theo chiều tăng dần.
Xoá hai điểm thấp nhất khỏi danh sách (nếu có nhiều điểm thấp nhất giống nhau, chỉ xoá giá trị nhỏ nhất).
In ra màn hình danh sách điểm còn lại sau khi đã xử lý.
Dữ liệu vào:
Dòng 1: Số nguyên n (số lượng bài kiểm tra, n ≥ 2)
Dòng 2: n số nguyên là điểm các bài kiểm tra (0 ≤ điểm ≤ 10)
Dữ liệu ra:
Một dòng duy nhất là danh sách điểm còn lại sau khi đã sắp xếp tăng dần và xoá 2 điểm nhỏ nhất, cách nhau bởi dấu cách.
"""


n = int(input())
A = list(map(int, input().split()))

A.sort()

min_score = A[0]

count = 0
res = []

for score in A:
    if score == min_score and count < 2:
        count += 1
    else:
        res.append(score)

print(*res)