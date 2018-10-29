class Sach():
    def __init__(self, ma, ten, ngay, don_gia, so_luong, nxb, tinh_trang):
        self.ma = ma
        self.ten = ten
        self.ngay = ngay
        self.don_gia = don_gia
        self.so_luong = so_luong
        self.nxb = nxb
        self.tinh_trang = tinh_trang
    def thanh_tien(self):
        if self.tinh_trang == "Moi":
            return self.so_luong * self.don_gia
        
            

class SachGiaoKhoa(Sach):


class SachThamKhao(Sach):
    




