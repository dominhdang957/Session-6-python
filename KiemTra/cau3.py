quantity_box = int(input("Nhập vào số thùng bạn muốn thêm: "))
total_quantity = 0
count = 0
for i in range(1,quantity_box + 1):
    quantity_product = int(input(f"Nhập số lượng thùng {i} muốn thêm: "))
    if quantity_product < 0: 
        print("Số lượng không hợp lệ")
    elif (quantity_product > 0):
        total_quantity += quantity_product
        count = count + 1
    elif quantity_product == 0:
        print("kết thúc chương trình.")
        break
print(f"Tổng số thùng hàng hợp lệ: {count}")
print(f"Tổng số sản phẩm thu được {total_quantity}")
