a = '뽀로로'
b = 23
c = '개발부'
d = 87.5

print('이름 : ' + a)      # + 기호가 문자열의 연결을 의미
print('나이 : ', b, '\n') # 서로 다른 자료형일 땐 + 말고 콤마(,) 사용
# print('나이 : ' + b + '\n') # 에러 : 서로 다른 자료형을 연결하려고 해서 발생
print('부서 : %s\n성적 : %.1f' % (c, d))
