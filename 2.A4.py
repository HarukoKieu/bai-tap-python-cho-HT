"""Tính Số Ngày Trong Tháng
Input Format
Hai số nguyên t và n lần lượt là tháng và năm.

Constraints
-10⁶ ≤ t, n ≤ 10⁶
Output Format
Nếu tháng hoặc năm không hợp lệ (không dương hoặc tháng không nằm trong [1, 12]), in ra "INVALID".
Ngược lại, in ra số ngày của tháng đó, xét tháng 2 có 29 ngày nếu là năm nhuận."""

t, n = map(int, input().split())
if t < 1 or t > 12 or n < 1:
    print("INVALID")
else:
    if t == 2:
        if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
            print(29)
        else:
            print(28)
    elif t in [4, 6, 9, 11]:
        print(30)
    else:
        print(31)