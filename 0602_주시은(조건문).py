'''
# 계산기 프로그램
#조건문
# if 조건 :
# elif 조건 :
# else :
a=float(input("a를 입력하세요:")) # input()은 문자열을 입력받는다
b=float(input("b를 입력하세요:"))
op=input("연산자를 입력하세요:")
if op=='+':
    c=a+b
    print(f"a+b={c}")
elif op=='-':
        c=a-b
        print(f"a-b={c}")
elif op=='*':
    c=a*b
    print(f"a*b={c}")
elif op=='/':
    c=a/b
    print(f'a/b={c}')
elif op=='//':
    c=a//b
    print(f'a//b={c}')
else:
    print("연산자 오류")
'''
'''
#음양수 판별 프로그램
c=int(input('숫자를 입력하세요:'))
if c>0:
  input('양수')
elif c<0:
  input('음수')
elif c==0:
  input('0')
'''
'''
#123pg
#반복문 복습
money=3000
card=True
if money>=3600 and card:
    print("택시타고 가라")
else:
    print('걸어가라')
'''
'''
#성적 관리 프로그램
# A : 100~91
# B : 90~81
# C : 80~71
# D : 70~61
# F : 60~
# 입력 : 점수, 출력 : 등급
score=int(input('점수를 입력하세요: '))
if 100>=score and 91<=score:
    grade='A'
    print('잘했어요')
elif 90>=score and 81<=score:
    grade='B'
elif 80>=score and 71<=score:
    grade='C'
elif 70>=score and 61<=score:
    grade='D'
elif 60>=score:
    grade='F'
    print('재수강하세요')
print(f'점수 = {score} , 등급={grade}')
'''
import random # random 패키지 사용
num=int(input('숫자를 입력하세요:'))
f=random.randrange(1, 101) # 1이상 101미만의 숫자를 랜덤 생성
if f==num:
    print('정답')
else:
    print('오답')
print(f"정답은 {f}입니다")
