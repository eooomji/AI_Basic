yn='\0'     # 널문자, 문자형 변수 초기화

while True:
    yn = input('다시 실행할까요? (y/Y) : ')
    if yn=='y' or yn=='Y':
        continue
    else:
        break

print('수고하셨습니다')
