"""Chuyển Đổi Kiểu Chữ Ký Tự
Input Format
Một dòng chứa 1 ký tự duy nhất cần kiểm tra và chuyển đổi.

Output Format
Nếu ký tự là chữ cái in thường, in ra chữ cái in hoa tương ứng.
Nếu ký tự là chữ cái in hoa, in ra chữ cái in thường tương ứng.
Nếu không phải là chữ cái, in ra chính ký tự đó (không thay đổi).
"""

s = input()
print(s.swapcase())