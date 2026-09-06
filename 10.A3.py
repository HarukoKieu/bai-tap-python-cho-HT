"""Đề bài:

Viết chương trình khai báo lớp Sinh Viên gồm các thông tin:

Mã SV
Họ tên
Lớp
Ngày sinh
Điểm GPA (số thực, kiểu double)
Yêu cầu:

Tạo hàm khởi tạo không tham số: gán các thuộc tính chuỗi bằng xâu rỗng "", số bằng 0.
Đọc thông tin của 1 sinh viên từ bàn phím và in ra màn hình.
Mã SV mặc định = SV001.
Chuẩn hóa ngày sinh về dạng chuẩn dd/mm/yyyy.
Input:

Gồm 4 dòng lần lượt là:

name: Họ tên sinh viên
className: Lớp
dob: Ngày sinh (có thể nhập dạng d/m/yyyy, dd/m/yyyy, …)
gpa: Điểm GPA (số thực)
Constraints:

Không ràng buộc.
Output:

In ra thông tin sinh viên trên một dòng, các trường cách nhau 1 dấu cách:
MãSV HọTên Lớp NgàySinh GPA
Trong đó GPA lấy 1 chữ số sau dấu phẩy thập phân."""

class SinhVien:
    def __init__(self):
        self.ma_sv = "SV001"
        self.ho_ten = ""
        self.lop = ""
        self.ngay_sinh = ""
        self.gpa = 0.0

    def nhap_thong_tin(self):
        self.ho_ten = input().strip()
        self.lop = input().strip()
        self.ngay_sinh = input().strip()
        self.gpa = float(input())

    def chuan_hoa_ngay_sinh(self):        
        parts = self.ngay_sinh.split('/')
        if len(parts) == 3:
            day = parts[0].zfill(2)
            month = parts[1].zfill(2)
            year = parts[2]
            self.ngay_sinh = f"{day}/{month}/{year}"

    def in_thong_tin(self):
        print(f"{self.ma_sv} {self.ho_ten} {self.lop} {self.ngay_sinh} {self.gpa:.1f}")
        

sv = SinhVien()
sv.nhap_thong_tin()
sv.chuan_hoa_ngay_sinh()
sv.in_thong_tin()