"""Nhập ngày sinh của một người theo dạng ngày/tháng/năm.Bạn hãy chuẩn hóa ngày sinh này về đúng dạng dd/mm/yyyy. Ví dụ nếu ngày sinh là 7/9/2000 thì được chuẩn hóa thành 07/09/2000.

Input Format
Nhập vào 1 xâu là ngày sinh của 1 người.

Constraints
.

Output Format
In ra ngày sinh đã được chuẩn hóa.

hàm zfill() trong Python sẽ trả về một bản sao của chuỗi gốc, nhưng với các ký tự '0' được thêm vào bên trái để đạt được độ dài mong muốn. Nếu chuỗi gốc đã có độ dài bằng hoặc lớn hơn độ dài mong muốn, nó sẽ trả về chuỗi gốc mà không thay đổi gì.
"""

s = input().strip()
d, m, y = s.split("/")
d = d.zfill(2)
m = m.zfill(2)
print(f"{d}/{m}/{y}")