"""Cho xâu kí tự S gồm các từ được phân cách nhau bởi một vài dấu cách.Bạn hãy kiểm tra xem trong xâu S có từ nào là xâu đối xứng và in từ đó ra.

Input Format
Nhập xâu S không quá 1000 kí tự.

Constraints
.

Output Format
In ra các từ đối xứng trong xâu, mỗi từ cách nhau 1 dấu cách.
"""
s = input()
words = s.split()
for word in words:
    if word == word[::-1]:
        print(word, end=' ')
        
# Cách 2: Sử dụng list comprehension
s = input()
palindromic_words = [word for word in s.split() if word == word[::-1]]
print(' '.join(palindromic_words))