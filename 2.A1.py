"""Tính Toán Hai Số Nguyên
Input Format
Một dòng chứa hai số nguyên a và b.

Constraints
-10⁹ ≤ a, b ≤ 10⁹
Output Format
In ra 4 dòng lần lượt là:

Tổng của a và b
Hiệu của a và b
Tích của a và b
Thương của a chia b (lấy chính xác 2 chữ số thập phân)
Nếu phép chia không hợp lệ (chia cho 0), in ra INVALID ở dòng cuối cùng.
"""

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
if b == 0:
    print("INVALID")
else:
    print(f"{a / b:.2f}")