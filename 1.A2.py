"""
Tính Giá Trị Biểu Thức A(x)
Cho biểu thức:

A(x) = x^3 + 3x^2 + x + 1
Với giá trị x được nhập từ bàn phím, hãy tính và in ra giá trị của biểu thức trên.

Input Format
Một dòng duy nhất chứa số nguyên dương x.

Constraints
0 ≤ x ≤ 10^5
Output Format
In ra giá trị của biểu thức A(x)
"""

x = int(input())
print(x**3 + 3*x**2 + x + 1)