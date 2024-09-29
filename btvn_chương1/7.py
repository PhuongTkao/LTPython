class Date:
    def __init__(self, ngay=1, thang=1, nam=2000):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def la_nam_nhuan(self):
        if (self.nam % 4 == 0 and self.nam % 100 != 0) or (self.nam % 400 == 0):
            return True
        return False

    def so_ngay_trong_thang(self):
        if self.thang in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.thang in [4, 6, 9, 11]:
            return 30
        elif self.thang == 2:
            if self.la_nam_nhuan():
                return 29
            else:
                return 28

    def hien_thi(self):
        print(f"{self.ngay:02d}/{self.thang:02d}/{self.nam}")

    def ngay_tiep_theo(self):
        if self.ngay < self.so_ngay_trong_thang():
            self.ngay += 1
        else:
            self.ngay = 1
            if self.thang < 12:
                self.thang += 1
            else:
                self.thang = 1
                self.nam += 1

ngay_hien_tai = Date(28, 2, 2024)  
ngay_hien_tai.hien_thi()  

ngay_hien_tai.ngay_tiep_theo()  
ngay_hien_tai.hien_thi()  

ngay_hien_tai.ngay_tiep_theo()  
ngay_hien_tai.hien_thi()  
