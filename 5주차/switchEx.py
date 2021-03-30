'''
파이썬은 switch-case가 없음
dictionary를 이용해 switch 같은 기능을 사용
'''

def switch(x):
    return {
        'one':1,
        'two':2,
        'three':3
    }.get(x, 9) # x값이 없으면 9를 출력

print(switch('two'))
print(switch('aaa'))
