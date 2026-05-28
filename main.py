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
            for i in range(1,4 + 1):
                print(f"Số lượng tồn kho của Laptop: ", " * ", end="")
            for i in range(1,qty_phone + 1):
                print(f"Số lượng tồn kho của Phone: ", "*", end="")
            for i in range(1,qty_tablet + 1):
                print(f"Số lượng tồn kho của Tablet: ", "*", end="")
            
