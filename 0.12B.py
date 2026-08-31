"""Xây dựng chương trình Python tạo một biến password cho trước. Hãy nhập vào mật khẩu từ người dùng và kiểm tra:

Nếu mật khẩu vừa nhập trùng khớp với biến password, in ra:

Đăng nhập thành công
Nếu mật khẩu không khớp, in ra:

Mật khẩu không chính xác
và tiếp tục cho người dùng nhập lại đến khi đúng mới dừng lại.
"""

password = "123456"
while True:
    user_input = input()
    if user_input == password:
        print("Đăng nhập thành công")
        break
    else:
        print("Mật khẩu không chính xác")