"""Xây dựng chương trình Python nhập vào một số nguyên dương n. Hãy xử lý và in ra màn hình các số chẵn từ 1 đến n (bao gồm n nếu là số chẵn), cách nhau bởi một dấu cách.

Dữ liệu vào:
Một số nguyên dương n (1 ≤ n ≤ 10⁶)
Dữ liệu ra:
Một dòng duy nhất gồm các số chẵn từ 1 đến n, cách nhau bởi dấu cách"""

# Cách 1: Sử dụng vòng lặp for và hàm range() để in ra các số chẵn từ 2 đến n.
n = int(input())
for i in range(2, n + 1, 2):
    print(i, end=" ")
    
# Cách 2: Sử dụng list comprehension với hàm join() để tạo danh sách các số chẵn và sau đó in ra.
n = int(input())
print(" ".join([str(i) for i in range(2, n + 1, 2)]))