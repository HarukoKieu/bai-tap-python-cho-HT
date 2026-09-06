"""Hãy viết một hàm tong(*args) để trả về tổng các số nguyên được truyền vào. Chương trình sẽ đọc:

Dòng 1: số nguyên N
Dòng 2: N số nguyên, cách nhau bởi khoảng trắng
Sau đó gọi hàm tong để tính tổng.

Input Format
Dòng 1: số nguyên N
Dòng 2: N số nguyên cách nhau bởi khoảng trắng

Constraints
1 ≤ N ≤ 10^5
Mỗi số nguyên thuộc đoạn [-10^9, 10^9]

Output Format
Một dòng duy nhất là tổng của N số."""

N = int(input())
a = list(map(int, input().split()))
print(sum(a))


# Cách 2: Sử dụng hàm tong(*args)
def tong(*args):
    return sum(args)

N = int(input())
a = list(map(int, input().split()))
print(tong(*a))