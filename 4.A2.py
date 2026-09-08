"""Đếm số lượng chữ cái, kí tự số, kí tự đặc biệt trong xâu.

Input Format
Xâu đầu vào không quá 1000 kí tự.

Constraints
.

Output Format
In kết quả số lượng chữ cái(không phân biệt hoa thường), kí tự số, kí tự đặc biệt trên 1 dòng."""

s = input()
alpha_count = 0
digit_count = 0
special_count = 0
for i in s:
    if i.isalpha():
        alpha_count += 1
    elif i.isdigit():
        digit_count += 1
    else:
        special_count += 1
print(alpha_count, digit_count, special_count)