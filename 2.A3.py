"""Kiểm Tra Năm Nhuận
Input Format
Một dòng chứa một số nguyên dương N.

Constraints
1 ≤ N ≤ 5000
Output Format
In ra YES nếu N là năm nhuận
Ngược lại in ra NO
Quy tắc năm nhuận:
Năm nhuận là:

Chia hết cho 400, hoặc
Chia hết cho 4 nhưng không chia hết cho 100
"""

n = int(input())
print("YES" if (n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)) else "NO")