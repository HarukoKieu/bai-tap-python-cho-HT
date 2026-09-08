"""Một nhân viên làm việc trong công ty được lưu lại các thông tin sau:

Mã nhân viên: được gán giá trị mặc định là 00001.
Họ tên: Xâu ký tự không quá 50 chữ cái.
Giới tính: Nam hoặc Nữ.
Ngày sinh: đúng theo chuẩn dd/mm/yyyy.
Địa chỉ: Xâu ký tự không quá 100 chữ cái.
Mã số thuế: Dãy số có đúng 10 chữ số.
Ngày ký hợp đồng: đúng theo chuẩn dd/mm/yyyy.
Viết chương trình nhập một nhân viên (không nhập mã) và in ra màn hình thông tin của nhân viên đó.

Input:

Gồm 6 dòng tương ứng với các thông tin từ 2 tới 7 (không nhập mã, mã mặc định là 00001).
Output:

In ra toàn bộ thông tin nhân viên (từ mã đến ngày ký hợp đồng), mỗi thông tin cách nhau đúng 1 dấu cách."""


class Employee:
    def __init__(self, full_name, gender, date_of_birth, address, tax_code, contract_signing_date):
        self.employee_id = "00001"
        self.full_name = full_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.address = address
        self.tax_code = tax_code
        self.contract_signing_date = contract_signing_date

    def __str__(self):
        return f"{self.employee_id} {self.full_name} {self.gender} {self.date_of_birth} {self.address} {self.tax_code} {self.contract_signing_date}"

    def enter_information(self):
        self.full_name = input().strip()
        self.gender = input().strip()
        self.date_of_birth = input().strip()
        self.address = input().strip()
        self.tax_code = input().strip()
        self.contract_signing_date = input().strip()

    def print_information(self):
        print(f"{self.employee_id} {self.full_name} {self.gender} {self.date_of_birth} {self.address} {self.tax_code} {self.contract_signing_date}")


employee = Employee("", "", "", "", "", "")
employee.enter_information()
employee.print_information()