from datetime import date

class Con_nguoi:
    # class Con_nguoi
    def __init__(self, ho_ten, ngay_sinh, gioi_tinh):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.gioi_tinh = gioi_tinh
    def in_thong_tin(self):
        chuoi = "Họ tên: " + self.ho_ten
        # format ngày tháng năm
        chuoi += "\nNgày sinh: " + self.ngay_sinh.strftime("%d/%m/%y")
        chuoi += "\nGiới tính: " + ("Nam" if self.gioi_tinh else "Nu")
        return chuoi

class Nhan_vien(Con_nguoi):
    # class Nhan_vien, ke thua tu class Con_nguoi
    luong_co_ban = 1300000
    counter = 1
    # constructor
    def __init__(self, ho_ten, ngay_sinh, gioi_tinh=True, he_so_luong=1.0):
        Con_nguoi.__init__(self,ho_ten, ngay_sinh, gioi_tinh)
        # tự động cấp phát id
        self.id = Nhan_vien.counter
        Nhan_vien.counter +=1
        self.he_so_luong = he_so_luong
        self.qua_trinh_tang_luong = []
        self.qua_trinh_tang_luong.append(he_so_luong)

    # hàm khởi tạo 1
    def init1(self, id, ho_ten, ngay_sinh):
        self.id = id
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh

    # hàm in thông tin
    def in_thong_tin(self):
        chuoi = "Id: " + str(self.id)
        chuoi += "\n" + Con_nguoi.in_thong_tin(self)
        chuoi += "\nHệ số lương: " + str(self.he_so_luong)
        # format tiền lương có dấu phẩy
        chuoi += "\nTiền lương: " + "{:,.0f}".format(self.tinh_luong())
        return chuoi

    # hàm tính lương
    def tinh_luong(self):
        return self.he_so_luong*Nhan_vien.luong_co_ban

    # hàm tăng lương
    def tang_luong(self, he_so_luong_moi):
        he_so_luong_cu = self.he_so_luong
        if he_so_luong_moi <= self.he_so_luong:
            print("Hệ số lương phải lớn hơn ", self.he_so_luong)
            return
        else:
            self.he_so_luong = he_so_luong_moi
            self.qua_trinh_tang_luong.append(he_so_luong_moi)

    # in quá trình tăng lương
    def in_qua_trinh(self):
        print(str(self.qua_trinh_tang_luong))

nhan_vien_1 = Nhan_vien("Nguyễn Văn A",date(1990, 1, 12),True, 1)
print(nhan_vien_1.in_thong_tin())
print("\n")
# nhan_vien_1.tang_luong(3.1);
# print("Lương mới: " + str(nhan_vien_1.tinh_luong()))
# print(nhan_vien_1.in_thong_tin())
# print("\n")
nhan_vien_2 = Nhan_vien("Võ Văn B", date(1989,12,1))
print(nhan_vien_2.in_thong_tin())
nhan_vien_2.tang_luong(3.1);
nhan_vien_2.in_qua_trinh()
print("\n")
print(nhan_vien_2.in_thong_tin())