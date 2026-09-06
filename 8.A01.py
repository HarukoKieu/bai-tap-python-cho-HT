"""Đề bài
Cho một dãy các số nguyên, hãy chuyển đổi nó thành tuple và in ra kết quả.

Input Format
Một dòng gồm các số nguyên, cách nhau bởi khoảng trắng.
Constraints
Số lượng phần tử không vượt quá 100.
Output Format
Một tuple chứa các phần tử đã cho.
"""

a = tuple(map(int, input().split()))
print(a)