"""Cho một danh sách gồm N số nguyên. Hãy đếm số lượng phần tử chẵn trong danh sách.

Input Format:

Dòng đầu tiên chứa số nguyên N — số lượng phần tử trong danh sách.
Dòng thứ hai chứa N số nguyên, các số được phân tách bởi khoảng trắng.
Constraints:

1 ≤ N ≤ 1000
Mỗi phần tử trong danh sách thuộc đoạn [−10⁹, 10⁹]
Output Format:

Một số nguyên duy nhất là số lượng phần tử chẵn trong danh sách.
"""

# Cách 1: Sử dụng vòng lặp for
N = int(input())
a = list(map(int, input().split()))
count_even = 0
for x in a:
    if x % 2 == 0:
        count_even += 1
print(count_even)


# Cách 2: Sử dụng list comprehension và hàm sum
N = int(input())
a = list(map(int, input().split()))
count_even = sum(1 for x in a if x % 2 == 0)
print(count_even)

