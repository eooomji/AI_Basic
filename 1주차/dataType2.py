# 포맷팅 템플릿
user = '이름 : %s\n나이 : %d' % ('뽀로로', 23)
# 세 번째 퍼센트 기호(포맷팅 연산자)를 기준으로 앞부분을 포맷팅 템플릿,
# 포맷팅 연ㅅ나자 뒷부분을 대입할 값(매개변수 or 파라미터)
# %s(문자열), %d(정수값)는 변환 지시어라고 부름
# 매개변수가 복수개인 경우는 튜플로 묶어줘야 함

dept = '부서 : %s\n' % '개발부'
gender = '성별 : %c\n' % 'M'  # %c는 글자 한 개를 받아서 처리 => MM인 경우는 오류남
score = '점수 : %f\n' % 85.3  # %f는 부동소수점(floating point) 수
tall1 = '신장 : %F' % 183.4
tall2 = '신장 : %.2f' % 183.4 # 소수점 아래 둘째자리까지만 출력
tall3 = '신장 : %-10.2f' % 183.4 # 총 10자리 왼쪽 정렬, 소수점 아래 둘째자리까지만 출력
tall4 = '신장 : %10.2f' % 183.4 # 총 10자리 오른쪽 정렬, 소수점 아래 둘째자리까지만 출력

print(user)
print(dept)
print(gender)
print(score)
print(tall1)
print(tall2)
print(tall3)
print(tall4)
