"""Viết chương trình Python để duyệt qua một danh sách số nguyên A đã cho. Hãy tính và in ra tổng các số chẵn có trong danh sách đó.

Dữ liệu vào:
Một dòng chứa các số nguyên cách nhau bởi dấu cách, biểu diễn danh sách A (có thể rỗng)
Dữ liệu ra:
Một dòng duy nhất là tổng các số chẵn trong danh sách A
"""

# Cách 1: Sử dụng vòng lặp for và hàm sum()
A = list(map(int, input().split()))
s = 0
for i in A:
    if i % 2 == 0:
        s += i                                   
print(s)

# Cách 2: Sử dụng list comprehension với hàm sum()
A = list(map(int, input().split()))
print(sum(i for i in A if i % 2 == 0))

