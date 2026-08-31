"""
    Viết chương trình nhập vào một danh sách điểm số (mỗi điểm cách nhau bởi một dấu cách). Hãy kiểm tra:

Nếu trong danh sách có tồn tại điểm 10, thì in ra số lượng điểm 10.
Nếu không có điểm 10, in ra thông báo:

Bạn chưa có điểm 10
Dữ liệu vào:
Một dòng chứa các số nguyên là điểm số (mỗi điểm cách nhau bởi dấu cách). Danh sách có thể rỗng.
Dữ liệu ra:
Một dòng:

Nếu có điểm 10 → in ra số lượng điểm 10
Nếu không → "Bạn chưa có điểm 10"""

A = list(map(int, input().split()))
if 10 in A:
    print(A.count(10))
else:
    print("Bạn chưa có điểm 10")