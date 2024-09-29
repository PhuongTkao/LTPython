class Stack:
    def __init__(self, suc_chua):
        self.suc_chua = suc_chua  
        self.stack = []  

    def push(self, item):
        if len(self.stack) < self.suc_chua:
            self.stack.append(item) 
        else:
            print("Ngăn xếp đã đầy.")

    def pop(self):
        if self.stack:
            return self.stack.pop()  
        else:
            print("Ngăn xếp trống.")

def main():
    suc_chua = int(input("Nhập sức chứa của ngăn xếp: "))
    stack = Stack(suc_chua)

    while True:
        action = input("\nNhập 'push', 'pop', hoặc 'exit': ").strip()
        
        if action == "push":
            item = float(input("Nhập phần tử: "))
            stack.push(item)  
        elif action == "pop":
            item = stack.pop()  
            if item is not None:
                print("Đã lấy:", item)
        elif action == "exit":
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
