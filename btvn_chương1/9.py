class DaGiac:
    def tinh_chu_vi(self):
        raise NotImplementedError

    def tinh_dien_tich(self):
        raise NotImplementedError

class HinhBinhHanh(DaGiac):
    def __init__(self, canh_day, chieu_cao):
        self.canh_day = canh_day
        self.chieu_cao = chieu_cao

    def tinh_chu_vi(self):
        return 2 * (self.canh_day + self.chieu_cao)

    def tinh_dien_tich(self):
        return self.canh_day * self.chieu_cao

class HinhChuNhat(HinhBinhHanh):
    pass  

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

def main():
    canh_day = float(input("Nhập cạnh đáy hình bình hành: "))
    chieu_cao = float(input("Nhập chiều cao hình bình hành: "))
    hinh_binh_hanh = HinhBinhHanh(canh_day, chieu_cao)
    print("Hình bình hành - Chu vi:", hinh_binh_hanh.tinh_chu_vi())
    print("Hình bình hành - Diện tích:", hinh_binh_hanh.tinh_dien_tich())

    chieu_dai = float(input("\nNhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    hinh_chu_nhat = HinhChuNhat(chieu_dai, chieu_rong)
    print("Hình chữ nhật - Chu vi:", hinh_chu_nhat.tinh_chu_vi())
    print("Hình chữ nhật - Diện tích:", hinh_chu_nhat.tinh_dien_tich())

    canh = float(input("\nNhập cạnh hình vuông: "))
    hinh_vuong = HinhVuong(canh)
    print("Hình vuông - Chu vi:", hinh_vuong.tinh_chu_vi())
    print("Hình vuông - Diện tích:", hinh_vuong.tinh_dien_tich())

if __name__ == "__main__":
    main()
