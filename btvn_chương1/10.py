import math

class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a  
        self.b = b  

    def tinh_dien_tich(self):
        return math.pi * self.a * self.b

class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh)  

    def tinh_dien_tich(self):
        return math.pi * self.a ** 2  

def main():
    x = float(input("Nhập tọa độ x của tâm elip: "))
    y = float(input("Nhập tọa độ y của tâm elip: "))
    a = float(input("Nhập bán trục lớn (a): "))
    b = float(input("Nhập bán trục nhỏ (b): "))
    
    elip = Elip(x, y, a, b)
    print("Diện tích elip:", elip.tinh_dien_tich())

    ban_kinh = float(input("\nNhập bán kính đường tròn: "))
    duong_tron = DuongTron(x, y, ban_kinh)
    print("Diện tích đường tròn:", duong_tron.tinh_dien_tich())

if __name__ == "__main__":
    main()
