"""Tính Khoảng Cách Giữa Hai Điểm Trong Mặt Phẳng Oxy
Input Format
Một dòng gồm 4 số nguyên x1 y1 x2 y2, là tọa độ của 2 điểm.

Constraints
-10^6 ≤ xi, yi ≤ 10^6
Output Format
Một dòng duy nhất là khoảng cách giữa 2 điểm, làm tròn đến 4 chữ số thập phân.
"""

x1, y1, x2, y2 = map(int, input().split())
print(f"{((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5:.4f}")