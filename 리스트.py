'''
list1 = ['abc', 'dfg', 'hij', 123, 456]
list1[1]='park'
print(list1)
'''
'''
arr = [4, 8, 12, 16, 20, 24, 28, 32]
print(arr)


#32= 4*8
arr1=[]
a=1
while True:
    if a==9: break
    arr1.append(4*a)
    a=a+1
print(arr1)
'''
'''
arr = [12,21,4,32,31]
size=len(arr) #리스트의 크기 변수
print(size)

idx=0 #인덱스 변수
while True:
    idx1=idx+1
    if idx1==size: break
    if arr[idx]>arr[idx1]:
        tmp = arr[idx]
        arr[idx]=arr[idx1]
        arr[idx1]=tmp
    idx=idx+1
    print(arr)
print('------------------')
print(sorted(arr))
print(list(reversed(arr)))
'''
'''
#내 생일 요일 찾기!
import datetime
today= datetime.datetime.now()
print(f'오늘은 {today.year}년도 입니당^*^')
print(f'오늘은 {today.month}월  입니당^3^')
print(f'오늘은 {today.day}일  입니당^~^')
if today.weekday() == 6:
    print('행복한 주말^0^')
else:
    print('오마이갓 평일-_-')
print('태어난 날의 요일 맞추깅><')
y = int(input('년을 입력하세융~: '))
m = int(input('달을 입력하세융~: '))
d = int(input('일을 입력하세융~: '))

date=datetime.datetime(y,m,d)

if date.weekday()==0: print('월요일~!')
elif date.weekday()==1: print('화요일~!')
elif date.weekday()==2: print('수요일~!')
elif date.weekday()==3: print('목요일~!')
elif date.weekday()==4: print('금요일~!')
elif date.weekday()==5: print('토요일~!')
elif date.weekday()==6: print('일요일~!')
'''
import random
#컴퓨터
while True:
    com=random.choice('RSP')  
    user=input('R, S, P 중 하나를 고르세용><:')
    if user==com :
        print('비겼슴당')
    elif (com=='R' and user=='P') or (com=='S' and user=='R') or (com=='P' and user=='S'):
        print('YOU WIN')
    elif  (user=='R' and com=='P') or (user=='S' and com=='R') or (user=='P' and com=='S'):
     print('YOU LOSE')

    print(f'컴퓨터 : {com}, 인간: {user}')





