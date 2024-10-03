class Student:
    #hàm khởi tạo đối tượng __init__
    count = 0
    def __init__(self, id,name):
        self.id = id
        self.name = name
        Student.count += 1
    # def set_id(self, id):
    #     self.id = id
    def get_id(self):
        return self.id    
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name    
    
    def show(self):
        print(f'ID: {self.get_id()}')        
        print(f'Name: {self.name}')     

# #Sử dụng class
# s= Student('01', 'Nguyen Tan Phat')
# s= Student('02', 'Ngo Gia Bao')
# print(Student.count)
