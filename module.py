import uuid
from tabulate import tabulate


class Transaction():
    id_trans = str(uuid.uuid4().fields[-1])[:5]

    def __init__(self):
        self.id = Transaction.id_trans
        self.orderItems = {}
        self.valError = 0
        print("Hello! Selamat datang di Betamart, id transaksi anda adalah {}".format(
            self.id))

    def add_item(self, item_name, item_qty, item_price):
        """
        Method untuk menambahkan barang yang ingin dibeli user kedalam rincian pembelian
        item_name = str
        item_qty = int
        item_price = int
        """
        self.item_name = item_name
        self.item_qty = item_qty
        self.item_price = item_price
        self.orderItems[item_name] = [item_qty, item_price]
        print('Penginputan berhasil!\n')

    def update_item_name(self, item_name, new_item_name):
        """
        Method untuk mengubah nama barang yang ingin dibeli user jika ada kesalahan penginputan
        item_name = str
        new_item_name = str
        """
        self.item_name = item_name
        self.new_item_name = new_item_name
        try:
            self.orderItems[new_item_name] = self.orderItems[item_name]
            del self.orderItems[item_name]
            print("Update nama item berhasil\n")
        except:
            print("Tidak dapat melakukan update nama item, nama item tidak ditemukan")

    def update_item_qty(self, item_name, new_item_qty):
        """
        Method untuk mengubah jumlah barang yang ingin dibeli user jika ada kesalahan penginputan
        item_name = str
        new_item_qty = int
        """
        self.item_name = item_name
        self.new_item_name = new_item_qty
        try:
            self.orderItems[self.item_name][0] = new_item_qty
            print("Update jumlah item berhasil\n")
        except:
            print("Tidak dapat melakukan update jumlah item, nama item tidak ditemukan")

    def update_item_price(self, item_name, new_item_price):
        """
        Method untuk mengubah harga barang yang ingin dibeli user jika ada kesalahan penginputan
        item_name = str
        new_item_price = int
        """
        self.item_name = item_name
        self.new_item_name = new_item_price
        try:
            self.orderItems[self.item_name][1] = new_item_price
            print("Update harga item berhasil\n")
        except:
            print("Tidak dapat melakukan update harga item, nama item tidak ditemukan")

    def delete_item(self, item_name):
        """
        Method untuk menghapus salah satu item yang sudah ada didalam rincian pembelian
        item_name = str
        """
        self.item_name = item_name
        try:
            del self.orderItems[item_name]
            print("Menghapus item berhasil\n")
        except:
            print("Tidak dapat menghapus item, nama item tidak ditemukan")

    def reset_transaction(self):
        """
        Method untuk menghapus seluruh item yang sudah ada didalam rincian pembelian
        """
        try:
            if not bool(self.orderItems):
                raise Exception
            else:
                self.orderItems.clear()
                print("Transaksi berhasil direset, semua item sudah dihapus")
        except Exception:
            print("Transaksi tidak bisa direset, tidak ada item pada order list")

    def total_price(self):
        """
        Method untuk mengetahui total harga yang harus dibayarkan user dengan beberapa ketentuan diskon
        """
        total_price_notdisc = 0
        priceErr = 0
        try:
            if self.valError == 0 or not bool(self.orderItems):
                priceErr = 1
                raise Exception
            elif self.valError != 0 and self.valError != 200:
                priceErr = 2
                raise Exception
            else:
                for k, v in self.orderItems.items():
                    item_total_price = v[0]*v[1]
                    total_price_notdisc += item_total_price
                priceErr = 0
        except Exception:
            if priceErr == 1:
                print("Rincian pesanan anda masih kosong, tidak dapat melihat total harga\nSilahkan lakukan penginputan data pemesanan terlebih dahulu\n")
            elif priceErr == 2:
                print("Terdapat kesalahan pada penginputan data di rincian pesanan anda, tidak dapat melihat total harga\nSilahkan melakukan pengecekan rincian pesanan dengan fungsi check_order\n")

        if (priceErr == 0 and total_price_notdisc > 200000 and total_price_notdisc <= 300000):
            print("Selamat anda mendapatkan diskon sebesar 5 %!")
            print("Total harga yang harus anda bayarkan adalah sebesar Rp. {}".format(
                total_price_notdisc - (total_price_notdisc*0.05)))
        elif (priceErr == 0 and total_price_notdisc > 300000 and total_price_notdisc <= 500000):
            print("Selamat anda mendapatkan diskon sebesar 8 %!")
            print("Total harga yang harus anda bayarkan adalah sebesar Rp. {}".format(
                total_price_notdisc - (total_price_notdisc*0.08)))
        elif (priceErr == 0 and total_price_notdisc > 500000):
            print("Selamat anda mendapatkan diskon sebesar 10 %!")
            print("Total harga yang harus anda bayarkan adalah sebesar Rp. {}".format(
                total_price_notdisc - (total_price_notdisc*0.1)))
        elif (priceErr == 0 and total_price_notdisc <= 200000):
            print("Total harga yang harus anda bayarkan adalah sebesar Rp. {}".format(
                total_price_notdisc))
        else:
            pass

    def check_orders(self):
        """
        Method untuk mengecek item yang sudah ada didalam rincian pembelian, sekaligus memberitahu user jika ada penginputan yang tidak
        sesuai dengan ketentuan yang ada
        """
        orderList = []
        headerTable = ["No", "Nama Item",
                       "Jumlah Item", "Harga/Item", "Total Harga"]

        n = 0
        checknum = 0

        for k, v in self.orderItems.items():
            checknum += 1
            noTable = n+1
            item_name = k
            item_qty = v[0]
            item_price = v[1]

            try:
                if not bool(self.orderItems):
                    self.valError = 0
                    raise Exception
                    raise Exception
                elif item_qty <= 0 and item_price <= 0:
                    self.valError = 1
                    raise Exception
                elif item_qty <= 0:
                    self.valError = 2
                    raise Exception
                elif item_price <= 0:
                    self.valError = 3
                    raise Exception
                else:
                    item_total_price = v[0]*v[1]
                    tableData = [noTable, item_name, item_qty,
                                 item_price, item_total_price]
                    orderList.append(tableData)
                    n += 1
                    self.valError = 200
            except Exception:
                if self.valError == 0:
                    print(
                        "Rincian pesanan anda masih kosong, silahkan masukkan item pesanan anda\n")
                    break
                elif self.valError == 1:
                    print("Item {} tidak dapat ditambahkan, jumlah dan harga item yang di input harus lebih besar daripada 0\n".format(
                        item_name))
                    continue
                elif self.valError == 2:
                    print("Item {} tidak dapat ditambahkan, jumlah item yang di input harus lebih besar daripada 0\n".format(
                        item_name))
                    continue
                elif self.valError == 3:
                    print("Item {} tidak dapat ditambahkan, harga item yang di input harus lebih besar daripada 0\n".format(
                        item_name))
                    continue

        if self.valError == 0:
            print("Berikut ini rincian pesanan anda:")
            print(tabulate(orderList, headers=headerTable, tablefmt="grid"))
        elif self.valError == 200 and (n == checknum):
            print("Pemesanan sudah benar\n")
            print("Berikut ini rincian pesanan anda:")
            print(tabulate(orderList, headers=headerTable, tablefmt="grid"))
        else:
            print("Berikut ini rincian pesanan anda:")
            print(tabulate(orderList, headers=headerTable, tablefmt="grid"))
            print("\nTerdapat kesalahan input data, silahkan lakukan update data yang tidak dapat ditambahkan sesuai pesan diatas\nJika butuh bantuan silahkan gunakan perintah bantuan")
