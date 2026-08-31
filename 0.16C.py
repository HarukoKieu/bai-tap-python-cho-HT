"""Định Dạng Ngày Tháng Năm
Bài toán giúp học sinh rèn luyện kỹ năng xử lý chuỗi và phân tách dữ liệu bằng dấu phân cách (/) trong Python.

Đề bài:
Viết chương trình Python nhập vào từ bàn phím một xâu s đại diện cho một ngày/tháng/năm theo định dạng dd/mm/yyyy. Trong đó:

dd: hai ký tự biểu diễn ngày,
mm: hai ký tự biểu diễn tháng,
yyyy: bốn ký tự biểu diễn năm.
Hãy xử lý và in ra chuỗi theo định dạng:


Ngày dd tháng mm năm yyyy
Dữ liệu vào:
Một dòng chứa chuỗi s có định dạng dd/mm/yyyy
Dữ liệu ra:
Một dòng theo định dạng: Ngày dd tháng mm năm yyyy
"""

s = input()
print(f"Ngay {s[0:2]} thang {s[3:5]} nam {s[6:10]}")