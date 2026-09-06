"""Xây dựng lớp HọcSinh gồm các thuộc tính: Họ tên, Ngày sinh, Điểm 3 môn Toán, Lý, Hóa. Tiến hành nhập thông tin một học sinh từ bàn phím và in ra thông tin gồm: họ tên, ngày sinh, tổng điểm 3 môn (lấy 1 chữ số sau dấu phẩy).

Input:

Dòng 1: Họ tên (không quá 100 ký tự)
Dòng 2: Ngày sinh (không quá 100 ký tự)
Dòng 3, 4, 5: Điểm Toán, Lý, Hóa (số thực hệ số 10)
Output:

In ra thông tin của học sinh, mỗi thông tin cách nhau đúng 1 dấu cách, theo thứ tự: Họ_tên Ngày_sinh Tổng_điểm
Constraints:

0.0 ≤ điểm mỗi môn ≤ 10.0
Kết quả tổng điểm được làm tròn 1 chữ số sau dấu phẩy.

Sample Input 1:

Nguyễn Văn A
01/01/2010
9.0
9.0
9.0
Sample Output 1:

Nguyễn Văn A 01/01/2010 27.0"""

class HocSinh:
    def __init__(self, ho_ten, ngay_sinh, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tong_diem(self):
        return round(self.diem_toan + self.diem_ly + self.diem_hoa, 1) 

ho_ten = input()
ngay_sinh = input()
diem_toan = float(input())
diem_ly = float(input())
diem_hoa = float(input())

hoc_sinh = HocSinh(ho_ten, ngay_sinh, diem_toan, diem_ly, diem_hoa)

print(hoc_sinh.ho_ten, hoc_sinh.ngay_sinh, hoc_sinh.tong_diem())
    