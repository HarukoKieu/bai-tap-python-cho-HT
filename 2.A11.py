"""Tìm Số Nhỏ Thứ 2 Trong 5 Số
Input Format
Một dòng gồm 5 số nguyên a, b, c, d, e (các số đều đôi một khác nhau).

Output Format
In ra số nhỏ thứ 2 trong 5 số đã cho.
"""

a, b, c, d, e = map(int, input().split())
print(sorted([a, b, c, d, e])[1])

# Cách 2: Sử dụng if-else
a, b, c, d, e = map(int, input().split())
if a < b and a < c and a < d and a < e:
    print(min(b, c, d, e))
elif b < a and b < c and b < d and b < e:
    print(min(a, c, d, e))
elif c < a and c < b and c < d and c < e:
    print(min(a, b, d, e))
elif d < a and d < b and d < c and d < e:
    print(min(a, b, c, e))
else:
    print(min(a, b, c, d))