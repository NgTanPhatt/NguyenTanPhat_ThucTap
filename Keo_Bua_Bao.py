from random import randint
print('Choose: Keo, Bua, Bao:')
player = input()
computer = randint(0,2)

if computer == 0:
    computer = 'Keo'
if computer == 1:
    computer = 'Bua'    
if computer == 2:
    computer = 'Bao'    

print('You choose: ' + player)
print('Computer choose: ' + computer)

if player == computer:
    print('Draw')
else:
        if player == 'Keo':
            if computer == 'Bua':
                print('Lose')
            else:
                print('Win')

        elif player == 'Bua':
            if computer == 'Bao':
                print('Lose')
            else:
                print('Win')      

        elif player == 'Bao':
            if computer == 'Keo':
                print('Lose')
            else:
                print('Win')
        else:
            print('Nhap Sai!')                          