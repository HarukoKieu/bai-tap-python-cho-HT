"""Viết chương trình kiểm tra một danh sách đầu vào xem có rỗng hay không.

Input Format:

Một dòng duy nhất chứa các phần tử, cách nhau bởi dấu cách (có thể là số hoặc chuỗi).
Dòng này có thể hoàn toàn rỗng.
Constraints:

Số lượng phần tử tối đa là 1000.
Output Format:

In ra "Empty" nếu danh sách rỗng.
Ngược lại, in ra "Not Empty".
"""


# Cách 1: Sử dụng vòng lặp for
a = input().split()
for i in a:
    if i != '':
        print("Not Empty")
        break
else:
    print("Empty")


# Cách 2: Sử dụng list comprehension
a = input().split()
print("Not Empty" if any(i for i in a) else "Empty")    