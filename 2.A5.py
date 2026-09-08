"""Phân Loại Tam Giác
Input Format
Một dòng chứa 3 số nguyên dương a, b, c — độ dài ba cạnh của tam giác.

Constraints
0 ≤ a, b, c ≤ 10³

Output Format
In ra:

1 nếu là tam giác đều
2 nếu là tam giác cân
3 nếu là tam giác vuông
4 nếu là tam giác thường
"INVALID" nếu ba cạnh không tạo thành một tam giác hợp lệ
"""

a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print(1)  # Tam giác đều
    elif a == b or b == c or a == c:
        print(2)  # Tam giác cân
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print(3)  # Tam giác vuông
    else:
        print(4)  # Tam giác thường
else:
    print("INVALID")  # Ba cạnh không tạo thành một tam giác hợp lệ