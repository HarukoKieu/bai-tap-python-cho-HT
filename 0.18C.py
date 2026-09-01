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

a = list(map(int, input().split()))

average = sum(a) / len(a)

unique = sorted(set(a), reverse=True)
if len(unique) >= 2:
    second = unique[1]
else:
    second = unique[0]

has_low = any(x <= 5 for x in a)

improved = [6 if x < 6 else x for x in a]

print(f"Trung bình cộng: {average:.2f}")
print(f"Điểm lớn thứ hai: {second}")
print(f"Có điểm dưới trung bình không: {'Có' if has_low else 'Không'}")
print("Danh sách điểm sau cải thiện:", *improved)