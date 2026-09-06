"""Đăng ký thông tin người dùng
Trong bài toán này, bạn sẽ thiết kế một chương trình Python để yêu cầu người dùng nhập thông tin cơ bản cho việc đăng ký tài khoản, bao gồm: tên, họ, và số điện thoại. Sau đó, chương trình sẽ hiển thị lại các thông tin đã nhập theo định dạng chuẩn.

Đề bài:
Viết chương trình Python yêu cầu người dùng nhập:

Tên (first name)
Họ (last name)
Số điện thoại (phone number)
Sau đó in ra kết quả như sau:

Your registered name is <first_name> <last_name>.
Your phone number is <phone_number>.
Dữ liệu vào:
3 dòng lần lượt là:

Tên (first name)
Họ (last name)
Số điện thoại
Dữ liệu ra:
2 dòng:

Dòng 1: Your registered name is <first_name> <last_name>.
Dòng 2: Your phone number is <phone_number>.
Ví dụ:
Dữ liệu vào:
Michael
Jordan
0987456123
Dữ liệu ra:
Your registered name is Michael Jordan.
Your phone number is 0987456123.
"""

first_name = input()
last_name = input()
phone_number = input()
print(f"Your registered name is {first_name} {last_name}.")
print(f"Your phone number is {phone_number}.")