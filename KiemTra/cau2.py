# câu 2
passwork = "123456"

for i in range(1,4):
    check_passwork = input("Nhập mật khẩu để đăng nhập: ")
    if check_passwork == passwork:
        print("Đăng nhập thành công!!")
        break
    else:
        print("Mật khẩu sai vui lòng nhập lại..")
if check_passwork != passwork:
    print("Tài khoản đã bị vô hiệu hóa")