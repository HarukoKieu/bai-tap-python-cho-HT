"""Cho số nguyên không âm N, hãy tiến hành sắp xếp các chữ số của N theo thứ tự tăng dần rồi in ra màn hình, trong trường hợp số sau khi sắp xếp xuất hiện các chữ số 0 ở đầu thì ra không in những chữ số 0 vô nghĩa này.

Input Format
Dòng duy nhất chứa số nguyên dương N (0<=N<=10^18)

Constraints
.

Output Format
In ra số N sau khi sắp xếp."""

n = int(input())
print(''.join(sorted(str(n))).lstrip('0') or '0')  # Sắp xếp các chữ số, loại bỏ các chữ số 0 ở đầu, nếu kết quả rỗng thì in ra '0'