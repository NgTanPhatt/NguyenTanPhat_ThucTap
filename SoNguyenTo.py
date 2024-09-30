print('So ban chon la: ')
n = int(input())

if n < 1:
        print('Vui long nhap so nguyen duong')
elif n < 2:
        print('Day khong phai la so nguyen to')    
else:
    for i in range(2, n//2 + 1):
        if n % i == 0:
            print('Day khong phai la so nguyen to')
            break
    else:
        print('day la so nguyen to')



