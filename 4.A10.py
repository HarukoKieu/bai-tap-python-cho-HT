"""Cho một xâu kí tự s ,hãy đếm tần suất xuất hiện của các kí tự trong xâu và in ra theo yêu cầu.

Input Format
Xâu kí tự có độ dài không quá 1000 chỉ bao gồm chữ cái.

Constraints
.

Output Format
Đầu tiên in ra các ký tự và tần suất xuất hiện của các ký tự ở trong xâu theo thứ tự từ điển tăng dần, sau đó cách ra một dòng và in ra tần suất xuất hiện của các ký tự theo thứ tự xuất hiện trong xâu(mỗi kí tự chỉ in 1 lần)

"""

s = input()

chars = set(s)

for c in sorted(chars):
    print(c, s.count(c))

print()

seen = set()

for c in s:
    if c not in seen:
        print(c, s.count(c))
        seen.add(c)
        
# Cách 2: Dùng dictionary để đếm tần suất xuất hiện của các ký tự trong xâu. cách này tối ưu hơn vì chỉ cần duyệt qua xâu một lần và lưu trữ tần suất xuất hiện của các ký tự trong một dictionary.

s = input()

freq = {}

for c in s:
    freq[c] = freq.get(c, 0) + 1

for c in sorted(freq):
    print(c, freq[c])

print()

seen = set()

for c in s:
    if c not in seen:
        print(c, freq[c])
        seen.add(c)