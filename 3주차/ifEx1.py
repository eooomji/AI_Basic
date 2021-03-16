string = 'korea'
if string == 'Korea':
    print("대한민국")
    print("한국")
    pass

print('Korea')  # 조건의 참 거짓과 상관없이 실행
print()

# ---------------------------------
score = 67
if score >= 60:
    print("합격")
    print("점수는", score, "점 입니다")
else:
    print("불합격")
    print("점수는", score, "점이며 다음 기회에...")

print("항상 실행됨 --")
print()

# if~ elif~ else문 ------------------
score = 95

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
    pass

print('점수는', score, '점이고 학점은', grade, '입니다')
print()

# 단순 if --------------
score = 70
if score >= 90 and score <= 100:
    grade = 'A'
if score >= 80 and score <= 90:
    grade = 'B'
if score >= 70 and score <= 80:
    grade = 'C'
if score >= 60 and score <= 70:
    grade = 'D'
if score >= 0 and score <= 60:
    grade = 'E'

print('점수는', score, '점이고 학점은', grade, '입니다')
print()
