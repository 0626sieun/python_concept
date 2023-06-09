'''
#1번
print(3==2)
print(4!=4)
print(5>=10)
'''
'''
#2번 과목 합격,불합격 프로그램
a=int(input('c언어 성적: '))
b=int(input('파이썬 성적: '))
c=int(input('자바 성적: '))
avg=a+b+c

if avg>=80:
    print('합격')
else:
    print('불합격')
'''
'''
#3번
a=int(input('양의 정수를 입력하세요:'))
if a%3==0 and a%2==0:
    print('3과 2의 배수')
elif a%3==0:
    print('3의 배수')
elif a%2==0:
    print('2의 배수')
else:
    print('2와 3의 배수가 아님')
'''
#4-1번 숫자 맞추기 게임
import random
ans=random.randrange(1,50) #0이상 10미만 숫자 랜덤 생성
c=0
while True:
    c=c+1
    me = int(input('숫자 입력:'))
    if ans<me:
        print('down')
        print(f'기회 : {c}')
    elif ans>me:
        print('up')
        print(f'기회 : {c}')
    else:
        print('정답')
        print(f'기회 : {c}')
        break
