"""Đếm Số Nguyên Trong Đoạn [a, b]
Input Format
Một dòng gồm 2 số thực a và b.

Output Format
In ra số lượng các số nguyên nằm trong đoạn [a, b] (kể cả a và b nếu là số nguyên).

"""

import math
a, b = map(float, input().split())
print(math.floor(b) - math.ceil(a) + 1)