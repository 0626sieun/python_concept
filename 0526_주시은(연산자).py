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
#음양수 판별 프로그램
c=int(input('숫자를 입력하세요:'))
if c>0:
  input('양수')
elif c<0:
  input('음수')
elif c==0:
  input('0')
