"""Kiểm Tra Số Fibonacci
Input Format
Một dòng chứa số nguyên không âm n.

Constraints
0 ≤ n ≤ 9×10¹⁸
Output Format
In ra YES nếu n là số Fibonacci.
Ngược lại in ra NO.

Công thức kiểm tra:
Một số n là số Fibonacci nếu:

5×n² + 4 hoặc 5×n² − 4 là số chính phương
"""

n = int(input())

if (5 * n * n + 4) ** 0.5 == int((5 * n * n + 4) ** 0.5) or (5 * n * n - 4) ** 0.5 == int((5 * n * n - 4) ** 0.5):
    print("YES")
else:
    print("NO")