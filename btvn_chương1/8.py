class Date:
    def __init__(self, ngay=1, thang=1, nam=2000):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def hien_thi(self):
        print(f"{self.ngay:02d}/{self.thang:02d}/{self.nam}")

class Employee:
    def __init__(self, ho_ten, ngay_sinh, ngay_vao_cong_ty):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh 
        self.ngay_vao_cong_ty = ngay_vao_cong_ty  

    def hien_thi_thong_tin(self):
        print("Họ tên:", self.ho_ten)
        print("Ngày sinh:", end=" ")
        self.ngay_sinh.hien_thi()
        print("Ngày vào công ty:", end=" ")
        self.ngay_vao_cong_ty.hien_thi()
        print("-" * 30)

class QuanLyNhanVien:
    def __init__(self):
        self.danh_sach_nhan_vien = []

    def them_nhan_vien(self, nhan_vien):
        self.danh_sach_nhan_vien.append(nhan_vien)

    def hien_thi_nhan_vien(self):
        for nhan_vien in self.danh_sach_nhan_vien:
            nhan_vien.hien_thi_thong_tin()

quan_ly = QuanLyNhanVien()

ngay_sinh1 = Date(1, 6, 2005)  
ngay_vao_cong_ty1 = Date(15, 9, 2023)  
nhan_vien1 = Employee("Mỹ Nữ Xink Đẹmp", ngay_sinh1, ngay_vao_cong_ty1)

ngay_sinh2 = Date(20, 12, 2005)  
ngay_vao_cong_ty2 = Date(1, 1, 2024)  
nhan_vien2 = Employee("Tiên cá bíc đi", ngay_sinh2, ngay_vao_cong_ty2)

quan_ly.them_nhan_vien(nhan_vien1)
quan_ly.them_nhan_vien(nhan_vien2)

quan_ly.hien_thi_nhan_vien()
