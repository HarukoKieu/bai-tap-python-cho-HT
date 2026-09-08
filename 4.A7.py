"""Cho xâu kí tự S, tiến hành sắp xếp kí tự trong xâu S theo thứ tự giảm dần, tăng dần theo thứ tự từ điển rồi in ra màn hình.

Input Format
Dòng duy nhất chứa xâu S không quá 1000 kí tự.

Constraints
.

Output Format
Dòng 1 in ra xâu S sau khi sắp giảm dần. Dòng 2 in ra xâu S sau khi sắp tăng dần.
"""

s = input()
print(''.join(sorted(s, reverse=True)))
print(''.join(sorted(s)))