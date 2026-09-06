"""Kiểm Tra Một Số Có Số Lượng Ước Là Số Lẻ
Input Format
Một dòng chứa số nguyên dương N.

Constraints
1 ≤ N ≤ 2×10¹⁸
Output Format
In ra YES nếu N có số lượng ước số là số lẻ.
Ngược lại in ra NO.

Công thức kiểm tra:
Một số N có số lượng ước số là số lẻ nếu và chỉ nếu N là số chính phương."""

import math
n = int(input())

if math.sqrt(n) == int(math.sqrt(n)):
    print("YES")
else:
    print("NO")