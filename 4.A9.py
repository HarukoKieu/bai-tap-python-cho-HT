"""Cho một xâu kí tự S bao gồm các chữ cái và dấu cách,hãy liệt kê các từ khác nhau trong xâu S, đầu tiên hãy liệt kê các từ khác nhau theo thứ tự từ điển tăng dần, sau đó cách một dấu cách rồi liệt kê các từ theo thứ tự xuất hiện trong xâu.

Input Format
Dòng duy nhất chứa xâu S có độ dài không quá 1000 kí tự.

Constraints
.

Output Format
Dòng đầu tiên in ra các trong xâu theo thứ tự từ điển. Dòng thứ hai in ra các từ theo thứ tự xuất hiện trong xâu.
"""

s = input()
words = s.split()  
print(' '.join(sorted(set(words))))
order = []
seen = set()
for word in words:
    if word not in seen:
        order.append(word)
        seen.add(word)
print(' '.join(order))  
        
        
        