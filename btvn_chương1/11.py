import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a  
        self.b = b  
        self.c = c  

    def tinh_chu_vi(self):
        return self.a + self.b + self.c

    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class TamGiacCan(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, b)  

class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, math.sqrt(a**2 + b**2)) 

class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a)  

def main():
    a = float(input("Nhập cạnh a của tam giác: "))
    b = float(input("Nhập cạnh b của tam giác: "))
    c = float(input("Nhập cạnh c của tam giác: "))
    tam_giac = TamGiac(a, b, c)
    print("Tam giác - Chu vi:", tam_giac.tinh_chu_vi())
    print("Tam giác - Diện tích:", tam_giac.tinh_dien_tich())

    a_vuong = float(input("\nNhập cạnh a của tam giác vuông: "))
    b_vuong = float(input("Nhập cạnh b của tam giác vuông: "))
    tam_giac_vuong = TamGiacVuong(a_vuong, b_vuong)
    print("Tam giác vuông - Chu vi:", tam_giac_vuong.tinh_chu_vi())
    print("Tam giác vuông - Diện tích:", tam_giac_vuong.tinh_dien_tich())

    a_deu = float(input("\nNhập cạnh a của tam giác đều: "))
    tam_giac_deu = TamGiacDeu(a_deu)
    print("Tam giác đều - Chu vi:", tam_giac_deu.tinh_chu_vi())
    print("Tam giác đều - Diện tích:", tam_giac_deu.tinh_dien_tich())

if __name__ == "__main__":
    main()
