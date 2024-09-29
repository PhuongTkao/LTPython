class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so if mau_so != 0 else 1  

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        while self.mau_so == 0:
            print("Mẫu số phải khác 0, vui lòng nhập lại.")
            self.mau_so = int(input("Nhập mẫu số: "))

    def in_phan_so(self):
        if self.mau_so == 1:
            print(self.tu_so)
        elif self.tu_so == 0:
            print(0)
        else:
            print(f"{self.tu_so}/{self.mau_so}")

def main():
    phan_so = PhanSo()
    phan_so.nhap_phan_so()
    print("Phân số vừa nhập là: ", end="")
    phan_so.in_phan_so()

if __name__ == "__main__":
    main()
