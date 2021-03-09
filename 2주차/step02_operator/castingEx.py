pay = 857650
tax = 0.033

rPay=pay-(pay*tax)  # 급여 = 급여-(급여*세금)
print('실 수령액 :', rPay)
print('실 수령액:', int(rPay))

# ---------------------------------------

# k = 87; e = 88; m = 75
#
# tot=k+e+m
# avg=tot/3
#
# print('총점 : ', tot)
# print('평균 : %.2f' % avg)

# ---------------------------------------

# a = 73.45
# b = int(a)      # 형변환 : 실수 --> 정수형변환
#
# print(a, ' ', b)    # 73.45   73
#
# c = '73.45'
#
# print(int(c))       # runtime 오류 발생
# print(int(float(c)))    # 실수형 문자열은 실수로 변환한 후 정수로 변환환
