'''
for 변수 in 자료구조(튜플, 리스트, 문자열):
    수행할 문장1
    수행할 문장2
    ...
'''

hap = 0
even = 0
odd = 0

for i in range(101):        # range(0:101) : 0~100까지
    hap += i
    if i%2==0:
        even += i
    else:
        odd += i

print('1~100까지의 합 : ',hap)
print('1~100까지의 짝수합 : ',even)
print('1~100까지의 홀수수합 : ',odd)

#-----------------------------------

num = range(101)
print(sum(num))     # sum() : 내장함수, built-in-method

#---------------------------------------

'''
문제. 65-90 사이의 임의의 정수 난수 10개를 만드세요 (for문으로)
'''

from random import randint

for i in range(10):
    print(randint(65,90), end=' ')
