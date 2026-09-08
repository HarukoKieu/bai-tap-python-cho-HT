"""Cho hai danh sách đã được sắp xếp tăng dần gồm N và M số nguyên. Hãy hợp nhất chúng thành một danh sách mới đã được sắp xếp tăng dần.

Input Format:

Dòng đầu tiên chứa hai số nguyên N và M.
Dòng thứ hai chứa N số nguyên (danh sách thứ nhất), sắp xếp tăng dần.
Dòng thứ ba chứa M số nguyên (danh sách thứ hai), sắp xếp tăng dần.
Constraints:

0 ≤ N, M ≤ 1000
Các phần tử thuộc đoạn [−10⁹, 10⁹]
Output Format:

Một dòng gồm các phần tử của danh sách đã hợp nhất, sắp xếp tăng dần, cách nhau bởi dấu cách.
"""

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0
res = []

while i < N and j < M:
    if a[i] < b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1

res.extend(a[i:]) 
res.extend(b[j:])

print(*res)