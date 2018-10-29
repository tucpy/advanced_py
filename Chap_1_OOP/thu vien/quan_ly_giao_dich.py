from datetime import datetime

#class GiaoDich duoc mac dinh la giao dich vang

class GiaoDich():
    def __init__(self,ma,ngay,don_gia,so_luong, loai):
        self.ma = ma
        self.ngay = ngay
        self.don_gia = don_gia
        self.so_luong = so_luong
        self.loai = loai

    def thanh_tien(self):
        return self.so_luong * self.don_gia

    def in_giao_dich(self):
        return self.ma + '-' + self.ngay + '-' + self.loai + '-' + str(self.so_luong) \
            + '-' + str(self.don_gia) + "- Thanh tien = " + str(self.thanh_tien())


#GiaoDichTienTe ke thua Giao dich vang, chi co bo sung them thuoc tinh 'mua'
class GiaoDichTienTe(GiaoDich):
    def __init__(self,ma,ngay,don_gia,so_luong, loai, mua):
        self.mua = mua
        GiaoDich.__init__(self,ma,ngay,don_gia,so_luong, loai)
    
    def thanh_tien(self):
        if self.mua:
            return GiaoDich.thanh_tien(self)
        else:
            return GiaoDich.thanh_tien(self) * 1.05

    def in_giao_dich(self):
        if self.mua:
            return "GD mua:" + GiaoDich.in_giao_dich(self)
        else:
            return "GD ban:" + GiaoDich.in_giao_dich(self)
        