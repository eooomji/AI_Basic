# 아규먼트(argument) : 프로그램 실행시의 파라미터
# python argvEx 10 20 30

# 세 수의 합 : 60

import sys

# 키보드로 입력하는 값은 모두 문자열
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

print('세 수의 합 : ',a+b+c)
