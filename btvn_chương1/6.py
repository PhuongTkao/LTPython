class Stack:
    def __init__(self, capacity):
        self.capacity = capacity  
        self.stack = []           
        self.top = -1             

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy. Không thể thêm phần tử.")
        else:
            self.top += 1
            self.stack.append(float(value))  
            print(f"Đã thêm {value} vào ngăn xếp.")

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng. Không thể lấy phần tử.")
            return None
        else:
            popped_value = self.stack.pop()
            self.top -= 1
            print(f"Đã lấy {popped_value} ra khỏi ngăn xếp.")
            return popped_value

    def count(self):
        return self.top + 1

    def print(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Nội dung ngăn xếp (từ trên xuống):")
            for i in range(self.top, -1, -1):  
                print(f"Phần tử {i + 1}: {self.stack[i]}")

    def display(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Ngăn xếp hiện tại:", self.stack)


stack = Stack(capacity=5)  

stack.push(1.2)
stack.push(2.3)
stack.push(3.4)

stack.print()  

stack.pop()
stack.print()  

stack.push(4.5)
stack.print()  