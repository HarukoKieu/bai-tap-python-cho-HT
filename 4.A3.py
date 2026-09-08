"""Cho một xâu kí tự chỉ bao gồm chữ số và chữ cái, hãy tính tổng các số xuất hiện trong xâu.

Input Format
Xâu đầu vào không quá 1000 kí tự.

Constraints
.

Output Format
In ra tổng chữ số xuất hiện trong xâu.
"""

import re

s = input()
print(sum(map(int, re.findall(r'\d+', s)))) # hàm re.findall() sẽ tìm tất cả các chữ số trong xâu và trả về một danh sách các chuỗi, sau đó map(int, ...) sẽ chuyển đổi các chuỗi này thành các số nguyên, và cuối cùng sum(...) sẽ tính tổng các số nguyên này.