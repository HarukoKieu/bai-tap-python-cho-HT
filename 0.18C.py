"""Phần Mềm Quản Lý Điểm Môn Tin Học của An
An đang đặt mục tiêu trở thành học sinh giỏi môn Tin học. Để làm được điều này, An cần theo dõi và cải thiện điểm số của mình một cách hiệu quả. Em hãy viết chương trình hỗ trợ An quản lý điểm với các chức năng sau:

Yêu cầu:
Tính trung bình cộng các số điểm mà An đã có.
Tìm ra số điểm lớn thứ hai trong danh sách điểm.
Kiểm tra xem danh sách điểm có điểm nào dưới trung bình (≤ 5) hay không.
Cải thiện các điểm < 6 thành 6.
Dữ liệu vào:
Một dòng chứa danh sách các điểm số, là các số nguyên từ 0 đến 10, cách nhau bởi dấu cách.
Dữ liệu ra:
Gồm 4 dòng:

Trung bình cộng: <giá trị làm tròn đến 2 chữ số thập phân>
Điểm lớn thứ hai: <giá trị>
Có điểm dưới trung bình không: Có hoặc Không
Danh sách điểm sau cải thiện: <các điểm đã được chỉnh sửa> (cách nhau bởi dấu cách)
"""

A = list(map(int, input().split()))
print("Trung binh cong:", round(sum(A) / len(A), 2))
A.sort()
print("Diem lon thu hai:", A[-2])
print("Co diem duoi trung binh khong:", "Co" if min(A) <= 5 else "Khong")
print("Danh sach diem sau khi cai tien:", " ".join(map(str, A)))