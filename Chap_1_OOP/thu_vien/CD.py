class CD():
    tong_tien = 0

    def __init__(self,ten,ca_si,so_bai_hat,gia_thanh):
        self.ten = ten
        self.ca_si = ca_si
        self.so_bai_hat = so_bai_hat
        self.gia_thanh = gia_thanh
        CD.tong_tien += self.gia_thanh

    def thong_tin_cd(self):
        return("#" + self.ten + "-" + self.ca_si + "-"\
            + str(self.so_bai_hat) + "-" + str(self.gia_thanh))