# câu 1
bill = float(input("Nhập vào đơn giá của sản phẩm: "))
quantity = int(input("Nhập vào số lượng mua: "))
total = bill * quantity
if total >= 1000000:
    discount = total * 0.1
    print("Giảm giá 10% trên tổng tiền.")
else:
    discount = 0

print(f"Số tiền khách phải thanh toán là {total - discount} VND")



# câu 3
