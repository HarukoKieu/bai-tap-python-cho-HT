"""Chuyển Đổi Nhiệt Độ từ Độ C Sang Độ F
Input Format
Nhập vào một số nguyên dương C là nhiệt độ đo theo độ C. (C không quá 10⁶)

Constraints
0 ≤ C ≤ 10^6

Output Format
Chuyển C sang độ F và in ra màn hình. Luôn in kết quả với 2 chữ số thập phân sau dấu chấm.

Công thức
F = (C × 9 / 5) + 32
"""

c = int(input())
f = (c * 9 / 5) + 32
print(f"{f:.2f}")
