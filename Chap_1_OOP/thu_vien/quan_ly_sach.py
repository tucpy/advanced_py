class Sach():
    def __init__(self, ma, ten, ngay, don_gia, so_luong, nxb):
        self.ma = ma
        self.ten = ten
        self.ngay = ngay
        self.don_gia = don_gia
        self.so_luong = so_luong
        self.nxb = nxb
    def tinh_thanh_tien(self):
        return self.so_luong * self.don_gia
    def in_sach(self):
        return self.ma + "-" + self.ten +"-" + self.nxb + "-" + self.ngay + "-" + str(self.don_gia) \
                + "-" + str(self.so_luong) + " - Thanh tien = " + str(self.tinh_thanh_tien())
        

class SachGiaoKhoa(Sach):
    sach_cu = 0
    sach_moi = 0
    #true (moi)/ false(cu)
    def __init__(self,ma, ten, ngay, don_gia, so_luong, nxb, tinh_trang):
        Sach.__init__(self, ma, ten, ngay, don_gia, so_luong, nxb)
        self.tinh_trang = tinh_trang
        if (self.tinh_trang):
            SachGiaoKhoa.sach_moi += self.so_luong
            SachGiaoKhoa.sach_cu += self.so_luong
    def tinh_thanh_tien(self):
        if (self.tinh_trang):
            return Sach.tinh_thanh_tien(self)
        else:
            return Sach.tinh_thanh_tien(self) * 0.5

class SachThamKhao(Sach):
    def __init__(self,ma, ten, ngay, don_gia, so_luong, nxb, thue):
        Sach.__init__(self,ma, ten, ngay, don_gia, so_luong, nxb)
        self.thue = thue
    def tinh_thanh_tien(self):
        return Sach.tinh_thanh_tien(self) + (Sach.tinh_thanh_tien(self) * self.thue /100)




