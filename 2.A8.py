"""Chữ Cái Kế Tiếp
Input Format
Một ký tự duy nhất.

Output Format
Nếu ký tự là chữ cái, in ra chữ cái kế tiếp theo bảng chữ cái ở dạng in thường.
Nếu ký tự là z hoặc Z, kết quả là a.
Nếu không phải là chữ cái, in ra INVALID.
"""

s = input()
if s.isalpha():
    if s.lower() == 'z':
        print('a')
    else:
        print(chr(ord(s.lower()) + 1))
else:
    print("INVALID")