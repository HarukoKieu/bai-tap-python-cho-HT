"""Đề bài:

Cho một danh sách gồm N phần tử (có thể là số nguyên, ký tự hoặc chuỗi). Hãy đảo ngược thứ tự các phần tử trong danh sách.

Input Format:

Dòng đầu tiên chứa số nguyên N — số lượng phần tử trong danh sách.
Dòng thứ hai chứa N phần tử, phân tách bởi khoảng trắng. (Mỗi phần tử là số nguyên hoặc chuỗi không chứa khoảng trắng.)
Constraints:

1 ≤ N ≤ 1000
Output Format:

In ra danh sách đã đảo ngược, các phần tử cách nhau bởi một dấu cách.
"""

N = int(input())
elements = input().split()
reversed_elements = elements[::-1]
print(" ".join(reversed_elements))              
