"""Kiểm Tra 10 Điều Kiện Trên Số Nguyên N
Input Format
Một dòng chứa một số nguyên dương N.

Constraints
1 ≤ N ≤ 10⁶
Output Format
In ra 10 dòng, mỗi dòng là YES hoặc NO ứng với 10 điều kiện sau:

N có phải là số chẵn?
N vừa chia hết cho 3 vừa chia hết cho 5?
N chia hết cho 3 nhưng không chia hết cho 7?
N chia hết cho 3 hoặc 7?
N lớn hơn 30 và nhỏ hơn 50?
N ≥ 30 và chia hết cho 2, 3 hoặc 5?
N là số có 2 chữ số và chữ số tận cùng là số nguyên tố (2, 3, 5, 7)?
N ≤ 100 và chia hết cho 23?
N không thuộc đoạn [10, 20]?
Chữ số tận cùng là bội số của 3 (0, 3, 6, 9)?"""

n = int(input())

# 1. N có phải là số chẵn?
print("YES" if n % 2 == 0 else "NO")

# 2. N vừa chia hết cho 3 vừa chia hết cho 5?
print("YES" if n % 3 == 0 and n % 5 == 0 else "NO")

# 3. N chia hết cho 3 nhưng không chia hết cho 7?
print("YES" if n % 3 == 0 and n % 7 != 0 else "NO")

# 4. N chia hết cho 3 hoặc 7?
print("YES" if n % 3 == 0 or n % 7 == 0 else "NO")

# 5. N lớn hơn 30 và nhỏ hơn 50?
print("YES" if 30 < n < 50 else "NO")

# 6. N ≥ 30 và chia hết cho 2, 3 hoặc 5?
print("YES" if n >= 30 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0) else "NO")

# 7. N là số có 2 chữ số và chữ số tận cùng là số nguyên tố (2, 3, 5, 7)?
print("YES" if 10 <= n <= 99 and int(str(n)[-1]) in [2, 3, 5, 7] else "NO")

# 8. N ≤ 100 và chia hết cho 23?
print("YES" if n <= 100 and n % 23 == 0 else "NO")

# 9. N không thuộc đoạn [10, 20]?
print("YES" if n < 10 or n > 20 else "NO")

# 10. Chữ số tận cùng là bội số của 3 (0, 3, 6, 9)?
print("YES" if int(str(n)[-1]) % 3 == 0 else "NO")