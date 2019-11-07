print(1+1)
print(1,'\n',2)
print('rlawndbs','\n','rlarlarla',sep="      ") 
print('Hello World')

a = 2					# 자료형을 선언할 필요가 없다 
print(a)

a = "asdasdasdad"
print(a)

a = 1.123123
print(a)

a = 'asd'
print(a)

a = input()			  # input은 무조건 문자형
print(type(a))
print(a + '123')	  # 문자 + 문자

a = int(input())	  # 정수형으로 입력 받는 방법
print(type(a))
print(a + 123)

print("안녕하세요라고 말했습니다")
print('안녕하세요라고 말했습니다')
print("'안녕하세요'라고 말했습니다")
print("\"안녕하세요\"라고 말했습니다")

print('안녕하세요'[0])
print('안녕하세요'[1])
print('안녕하세요'[2])
print('안녕하세요'[3])
print('안녕하세요'[4])

print('안녕하세요'[1:4])   # 1~3 까지 나옴 녕하세

alp = 'abcdefghijklmnopqrstuvwxyz'
print(alp[5:11])
print(alp[18:26])
print(alp[-8:])
print(len(alp))         # 배열의 길이 출력

a = 15
b = 8
print(a+b,a-b,a*b,a/b)
print('a + b = %d a - b = %d a * b = %d a / b = %f' % (a+b, a-b, a*b, a/b))
print(a//b, a/b, a**b)

tmp = ''
for i in alp:
	tmp += i
	print(tmp)
