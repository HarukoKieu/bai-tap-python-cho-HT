"""Cho một xâu S có không quá 1000 kí tự, thực hiện đếm số lượng từ trong xâu.

Input Format
Dòng duy nhất chứa xâu có không quá 1000 kí tự.

Constraints
.

Output Format
Số lượng từ trong xâu."""

s = input()
print(len(s.split()))  # Sử dụng split() để tách các từ và len() để đếm số lượng từ