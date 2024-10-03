from student import Student
sv = []
while True: #vòng lặp vô tận
    print('''
    Select:
    0. Exit      
    1. View list
    2. Add
    3. Delete  
    4. Edit                            
      ''')
    select = input('Which is function you choose?\n')
    if select.isdigit():
        select = int(select)
        if select == 0:
            break
        elif select ==1:   
            if len(sv) == 0:
                print('There are currently no students')
            else:
                for i in sv:
                    i.show()
        elif select ==2:
            id = input('Enter your student id: ')
            name = input('Enter your student name: ')
            sv.append(Student(id,name))     
        elif select ==3:
            id = input('Enter your student id: ')  
            for i in sv:
                if i.id==id:
                    sv.remove(i)
        elif select ==4:
            id = input('Enter your student id: ')  
            for i in sv:
                if i.id==id:
                    i.set_name(input('Name you want to change: '))
    else:
        print('Please select again')    