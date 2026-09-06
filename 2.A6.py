"""Phân Loại Ký Tự
Input Format
Một ký tự duy nhất.

Output Format
Nếu ký tự là chữ cái in hoa, in ra "UPPER"
Nếu ký tự là chữ cái in thường, in ra "LOWER"
Nếu ký tự là chữ số, in ra "DIGIT"
Nếu là ký tự đặc biệt, in ra "SPECIAL"
"""

s = input()
if s.isupper():
    print("UPPER")
elif s.islower():
    print("LOWER")
elif s.isdigit():
    print("DIGIT")
else:
    print("SPECIAL")