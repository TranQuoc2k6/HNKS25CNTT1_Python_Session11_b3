product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình
""")
    choice = input("Nhập lựa chọn của bạn: ")
    print()
    match choice:
        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                count_list = 0
                print("Danh sách sản phẩm hiện tại:")
                for emp in product_list:
                    count_list += 1
                    product_id = emp["product_id"]
                    product_name = emp["product_name"]
                    price = emp["price"]
                    quantity = emp["quantity"]
                    print(f"{count_list}. Mã SP: {product_id} | Tên: {product_name} | Giá: {price} | Số lượng: {quantity}")
        case "2":
            add_product = {}
            flag = 0
            input_product_id = input("- Nhập mã sản phẩm: ").strip().upper()
            
            for emp in product_list:
                if input_product_id == emp["product_id"]:
                    print("Mã sản phẩm đã bị trùng")
                    flag = 1
                    break
            if flag == 0:
                input_product_name = input("- Nhập tên sản phẩm: ").strip().capitalize()
    
                input_price = int(input("- Nhập giá sản phẩm: "))
                while input_price <= 0:
                    print("Giá sản phẩm phải là số dương")
                    input_price = int(input("- Nhập giá sản phẩm: "))

                input_quantity = int(input("- Nhập số lượng sản phẩm: "))
                while input_quantity <= 0:
                    print("Số lượng sản phẩm phải là số dương")
                    input_quantity = int(input("- Nhập số lượng sản phẩm: "))
                add_product["product_id"] = input_product_id
                add_product["product_name"] = input_product_name
                add_product["price"] = input_price
                add_product["quantity"] = input_quantity
                product_list.append(add_product)
                print("Thêm sản phẩm thành công")
        case "3":
            input_update_product_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
            flag = 0
            for emp in product_list:
                if input_update_product_id == emp["product_id"]:
                    flag = 1
                    input_update_product_name = input("Nhập tên sản phẩm mới: ").strip().capitalize()
                    input_update_price = int(input("Nhập giá sản phẩm mới: "))
                    input_update_quantity = int(input("Nhập số lượng sản phẩm mới: "))
                    emp["product_name"] = input_update_product_name
                    emp["price"] = input_update_price
                    emp["quantity"] = input_update_quantity
                    print("Sửa thông tin sản phẩm thành công")
            if flag == 0:
                print("Không tìm thấy mã sản phẩm cần cập nhật!”")

        case "4":
            input_delete_product_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
            index = -1
            flag = 0
            for emp in product_list:
                index += 1
                if input_delete_product_id == emp["product_id"]:
                    product_list.pop(index)
                    flag = 1
                    print("Đã xóa thành công")
            if flag == 0:
                print("Không tìm thấy mã sản phẩm cần xoá!")

        case "5":
            print("Thoát chương trình.Sau đó dừng chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")