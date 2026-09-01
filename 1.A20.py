"""Đếm Số Chính Phương Trong Đoạn [a, b]
Input Format
Một dòng chứa hai số nguyên dương a và b.

Constraints
1 ≤ a ≤ b ≤ 10¹⁸
Output Format
In ra số lượng các số chính phương trong đoạn [a, b].
"""

import math
a, b = map(int, input().split())
result = math.isqrt(b) - math.isqrt(a - 1)
print(result)