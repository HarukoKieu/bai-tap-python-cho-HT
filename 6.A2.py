"""Đề bài:

Cho một danh sách gồm N số nguyên. Hãy tìm phần tử lớn nhất trong danh sách.

Input Format:

Dòng đầu tiên chứa số nguyên N — số lượng phần tử trong danh sách.
Dòng thứ hai chứa N số nguyên, các số được phân tách bởi khoảng trắng.
Constraints:

1 ≤ N ≤ 1000
Mỗi phần tử trong danh sách thuộc đoạn [−10⁹, 10⁹]
Output Format:

Một số nguyên duy nhất là phần tử lớn nhất trong danh sách.
"""

N = int(input())
a = list(map(int, input().split()))
print(max(a))