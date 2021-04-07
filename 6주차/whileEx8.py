'''
문제. 65-90 사이의 임의의 정수 난수 10개를 만드세요
'''
from random import *

num = 0

while num<10:
    print(randint(65, 90), end=' ')
    num+=1
