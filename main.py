import module

trnsct_123 = module.Transaction()


def menu():
    print("\nSilahkan pilih salah satu menu dibawah ini")
    print("1. Add Item")
    print("2. Update Item Name")
    print("3. Update Item Qty")
    print("4. Update Item Price")
    print("5. Delete Item")
    print("6. Reset Transaction")
    print("7. Check Orders")
    print("8. Total Price")
    print("9. Keluar\n")


start = True
menu()
while start == True:
    try:
        pilihan = int(input("Choose menu: "))
        if pilihan == 1:
            item_name = str(input("Silahkan masukkan nama item: "))
            try:
                item_qty = int(input("Silahkan masukkan jumlah item: "))
                item_price = int(input("Silahkan masukkan harga item: "))
            except:
                print(
                    "Penginputan item GAGAL!\nJumlah dan harga item harus berupa angka")
            trnsct_123.add_item(item_name, item_qty, item_price)
            menu()
        elif pilihan == 2:
            item_name = str(input(
                "Silahkan masukkan nama item yang ingin diubah: "))
            new_item_name = str(
                input("Silahkan masukkan nama item yang baru: "))
            trnsct_123.update_item_name(item_name, new_item_name)
            menu()
        elif pilihan == 3:
            str(item_name=input(
                "Silahkan masukkan nama item yang ingin diubah: "))
            try:
                new_item_qty = int(
                    input("Silahkan masukkan jumlah item yang baru: "))
            except:
                print("Penginputan item GAGAL!\nJumlah item harus berupa angka")
            trnsct_123.update_item_qty(item_name, new_item_qty)
            menu()
        elif pilihan == 4:
            item_name = str(input(
                "Silahkan masukkan nama item yang ingin diubah: "))
            try:
                new_item_price = input(
                    "Silahkan masukkan harga item yang baru: ")
            except:
                print("Penginputan item GAGAL!\nHarga item harus berupa angka")
            trnsct_123.update_item_price(item_name, new_item_price)
            menu()
        elif pilihan == 5:
            item_name = str(input(
                "Silahkan masukkan nama item yang ingin dihapus: "))
            trnsct_123.delete_item(item_name)
            menu()
        elif pilihan == 6:
            trnsct_123.reset_transaction()
            menu()
        elif pilihan == 7:
            trnsct_123.check_orders()
            menu()
        elif pilihan == 8:
            trnsct_123.total_price()
            menu()
        elif pilihan == 9:
            start = False
            print("Transaksi selesai")
            break
        else:
            raise Exception
    except Exception:
        print("\nInput angka sesuai yang ada pada menu\n")
        menu()
