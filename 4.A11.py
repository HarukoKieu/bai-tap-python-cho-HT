"""Cho một xâu kí tự S, hãy tìm kí tự có số lần xuất hiện nhiều nhất ở trong xâu. Trong trường hợp có nhiều kí tự có cùng số lần xuất hiện lớn nhất thì in ra kí tự có thứ tự từ điển lớn nhất.

Input Format
Xâu kí tự S chỉ bao gồm chữ cái in hoa và in thường và không quá 1000 kí tự.

Constraints
.

Output Format
In ra từ có số lần suất hiện nhiều nhất và số lần xuất hiện tương ứng cách nhau 1 dấu cách."""

# lambda function để tìm kí tự có số lần xuất hiện nhiều nhất, trong trường hợp có nhiều kí tự có cùng số lần xuất hiện lớn nhất thì in ra kí tự có thứ tự từ điển lớn nhất.
s = input()
max_char = max(set(s), key=lambda c: (s.count(c), c)) 
print(max_char, s.count(max_char))

# Cách 2: Dùng dictionary

s = input()

seen = {}

for c in s:
    seen[c] = seen.get(c, 0) + 1

max_char = max(seen, key=lambda c: (seen[c], c))

print(max_char, seen[max_char])