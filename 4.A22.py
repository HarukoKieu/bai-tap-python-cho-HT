"""Một số được coi là số đẹp nếu nó có tất cả các chữ số là số nguyên tố và tổng các chữ số của nó cũng là số nguyên tố. Hãy viết chương trình kiểm tra số nguyên dương N cho trước có phải là số đẹp hay không?.Nếu phải in ra màn hình YES ngược lại in NO.

Input Format
Số nguyên dương N, không quá 1000 chữ số.

Constraints
.

Output Format
In ra đáp án bài toán."""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

digit_sum = 0
for c in str(n):
    if c not in '2357':
        print("NO")
        break
    digit_sum += int(c)
else:
    if is_prime(digit_sum):
        print("YES")
    else:
        print("NO")
