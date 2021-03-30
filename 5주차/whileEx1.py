'''
while문 : 조건이 참일 동안 문장을 반복 수행
while 조건식 :
    문장
    [탈출 조건]
'''

n= 10
while n>0:
    print(n, end='')
    n=n-1
print('마지막')

# n = 0
#
# while n < 3:
#     print('hello')
#     n = n + 1

# n = 0
#
# while True:     # 무한루프
#     n = n + 1
#     if n <= 5:
#         print(n)
#     else:
#         break
