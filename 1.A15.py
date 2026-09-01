"""A có n đô la trong tài khoản ngân hàng. Anh ấy muốn rút toàn bộ tiền mặt với ít tờ tiền nhất có thể.

Các mệnh giá tờ tiền có sẵn là: 1, 5, 10, 20, 100.

Input Format
Một số nguyên dương n

Constraints
1 ≤ n ≤ 10⁹
Output Format
Một dòng duy nhất in ra số tờ tiền tối thiểu để rút được n đô la.
"""

n = int(input())
count = 0
while n > 0:
    if n >= 100:
        count += n // 100
        n %= 100
    elif n >= 20:
        count += n // 20
        n %= 20
    elif n >= 10:
        count += n // 10
        n %= 10
    elif n >= 5:
        count += n // 5
        n %= 5
    else:
        count += n
        break
print(count)