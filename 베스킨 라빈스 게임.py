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
'''
#4-1번 숫자 맞추기 게임
import random
ans=random.randrange(1,10) #0이상 10미만 숫자 랜덤 생성
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
        '''
#베스킨 라빈스 31게임
import random
print('베스킨 라빈스 31게임><')
print('1~31의 숫자를 번갈아 불러 31을 부르는 사람이 지는 게임입니당!')

#변수 선언
number=0 #1부터 31까지 증가할 수
turn=0 #누구차례냐, 0+사용자, 1=컴퓨터

while True:
    if number>=31: break

    if turn ==0: #내차례만 여기를 실행하겠다.
        #부를 숫자 입력
        count=int(input('내가 부를 숫자 갯수(1~3) :'))
        if count>3:
            print('다시 입력하세융!!')
            continue
        while count!=0:
            count=count-1
            number=number+1
            print(f'나: {number}')
        turn=1

        
    elif turn==1:
        com_c=random.randrange(1,4)
        while com_c!=0:
            com_c=com_c-1
            number=number+1
            print(f'컴퓨터: {number}')
        turn=0
        
if turn ==0:
    print('승리!! 추카추카030')
elif turn ==1:
    print('패배ㅠㅜㅠㅜ')
