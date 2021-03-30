# 난수 함수 : 컴퓨터가 임의의 숫자를 발생시킴(의사 난수 ; pseudo random)

from random import *    # 생각해보니 여기서도 *은 모든을 의미했어...

print(random())         # 0 이상 1미만의 실수 난수
print(random() + 1.0)   # 1 이상 2 미만의 실수 난수, 원하는 숫자를 더해서 난수의 범위 조절
print(uniform(1.0, 3.14))   # 1 이상 3.14 미만의 실수 난수
print(randint(1, 100))      # 1 이상 100 이하의 실수 난수
print(randrange(1, 51, 3))  # 1 이상 51 미만. 1, 4, 7, 10 '''
print(choice([1,2,3,4,5,6]))    # []안의 값 중 하나를 리턴
print(sample(range(1,46), 6))   # 로또 번호 생성, 중복 값을 배제
