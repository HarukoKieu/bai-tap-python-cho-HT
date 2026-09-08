"""Cho một xâu S có không quá 1000 kí tự, thực hiện sắp xếp các từ trong xâu theo thứ tự từ điển tăng dần.

Input Format
Dòng duy nhất chứa xâu S không quá 1000 kí tự.

Constraints
.

Output Format
In ra các từ theo thứ tự từ điển tăng dần.
"""

s = input()
words = s.split()  
words.sort()                                              
print(' '.join(words))          