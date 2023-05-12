#2023.05.12
'''
a=int(input("a를 입력하세요:"))
b=int(input("b를 입력하세요:"))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a/b)
'''
'''
a=int(input("a를 입력하세요:"))
b=int(input("b를 입력하세요:"))

print("a=%d 입니다, b=%d입니다"%(a,b))
'''
#내가 희망하는 키 출력
name="주시은"
age=14
height=157
print("제이름은 %s입니다. \n 나이는 %d, 키는 %d." %(name , age ,height))
hope=int(input("희망하는 키를 작성해라:"))
print("제이름은 %s입니다. \n 나이는 %d, 희망하는키는 %d." %(name , age ,hope))
print("제이름은 {}입니다. \n나이는 {}, 희망키는 {}." .format (name, age,hope))

tmp=hope-height

print("그럼 앞으로 %d 만큼 커야겠네요ㅋ" %(hope-height))
print("그럼 앞으로 "+str(tmp)+"만큼 커야겠네요ㅋ")
