qty_laptop = 0;
qty_phone  = 0;
qty_tablet = 0;
while True:
    print("=" * 60)
    print("---- HỆ THỐNG QUẢN LÝ KHO HÀNG RIKKEI STORE ---")
    print("=" * 60)
    print("1. Show report quantity in store.")
    print("2. Import product in store.")
    print("3. Export product for foreign.")
    print("4. Error quantity in store lower.")
    print("5. Exit programme.")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1: 
            print(f"Laptop({qty_laptop}): "," * " * qty_laptop, end="")
            print()
            print(f"Phone({qty_phone}): "," * " * qty_phone, end="")
            print()
            print(f"Tablet({qty_tablet}): "," * " * qty_tablet, end="")
            print()
        case 2:
            print("---- HỆ THỐNG NHẬP HÀNG ----")
            print("1. Laptop.")
            print("2. Phone.")
            print("3. Tablet.")
            print("-" * 50)
            choose = int(input("Nhập lựa chọn của bạn: "))
            if choose == 1:
                import_laptop = int(input("Nhập số lượng laptop cần nhập: "))
                qty_laptop += import_laptop
            elif choose == 2:
                import_phone = int(input("Nhập số lượng phone muốn nhập: "))
                qty_phone += import_phone
            elif choose == 3:
                import_tablet = int(input("Nhập số lượng tablet muốn nhập: "))
                qty_tablet += import_tablet
            else:
                print("Không có chức năng này.!!")
        case 3: 
            print("---- HỆ THỐNG XUẤT HÀNG ----")
            print("1. Laptop.")
            print("2. Phone.")
            print("3. Tablet.")
            print("-" * 50)
            choosen = int(input("Nhập lựa chọn của bạn: "))
            if choosen == 1:
                export_laptop = int(input("Nhập số lượng laptop cần xuất: "))
                if(export_laptop > qty_laptop):
                    print("Số lượng tồn kho không đủ không thể xuất hàng.")
                else:
                    qty_laptop -= export_laptop
            elif choose == 2:
                export_phone = int(input("Nhập số lượng phone muốn xuất: "))
                if(export_phone > qty_phone):
                    print("Số lượng tồn kho không đủ không thể xuất hàng.")
                else:
                    qty_phone -= export_phone
            elif choose == 3:
                export_tablet = int(input("Nhập số lượng tablet muốn nhập: "))
                if (export_tablet > qty_tablet):
                    print("Số lượng tồn kho không đủ không thể xuất hàng.")
                else:
                    qty_tablet -= export_tablet
            else:
                print("Không có chức năng này.!!")
        case 4:
            if qty_laptop < 10:
                print(f"Mặt hàng Laptop sắp hết chỉ còn {qty_laptop} sản phẩm.")
            if qty_phone < 10:
                 print(f"Mặt hàng phone sắp hết chỉ còn {qty_phone} sản phẩm.")
            if qty_tablet < 10:
                 print(f"Mặt hàng tablet sắp hết chỉ còn {qty_tablet} sản phẩm.")
        case 5:
            print("KẾT THÚC CHƯƠNG TRÌNH... TẠM BIỆT")
            break
        case _:
            print("HỆ THỐNG KHÔNG CÓ CHỨC NĂNG NÀY..")

            

            
        
            
