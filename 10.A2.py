"""Hãy xây dựng một lớp Phân số gồm 2 thuộc tính là tử số và mẫu số (đều là số nguyên). Viết chương trình nhập vào một phân số và in ra phân số đó ở dạng tối giản.

Input:

Một dòng duy nhất chứa 2 số nguyên numerator và denominator, lần lượt là tử số và mẫu số.
Constraints:

1 ≤ numerator, denominator ≤ 2^63 - 1
Output:

In ra phân số ở dạng tối giản (tử và mẫu không còn ước chung nào ngoài 1).
"""

import math    
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def toi_gian(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    def __str__(self):
        return f"{self.tu}/{self.mau}"

tu, mau = map(int, input().split())
phan_so = PhanSo(tu, mau)
phan_so.toi_gian()
print(phan_so)
