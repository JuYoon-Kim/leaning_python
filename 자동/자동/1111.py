a = int(input("물건 값을 입력하시오: "))       # 거스름돈 나오는 프로그램 

x = y = z = 0

x = int(input("1000원 지폐의 개수: "))
y = int(input("500원 동전의 개수: "))
z = int(input("100원 동전의 개수: "))

b = (x*1000 + y*500 + z*100)

a = b - a

print("500원 = %d 100원 = %d 50원 = %d 10원 = %d  1원 = %d" % ((a//500), ((a%500)//100), ((a%100)//50), ((a%50)//10), ((a%10)//1)))

a = 10
b = 20
c = 30
d = 40

a,b = b,a
a,b,c,d = d,c,b,a
print(a,b,c,d)    # 40 30 10 20  = 만 적으면 대입 됨 

a = 10
b = 20
c = 30
d = 40

if (a > b):        # : 은 문장이 안 끝났다는 소리로 인터프리터 언어의 특징이다 들여쓰기 필수
	print("a가 더 큽니다")
else:
	print("b가 더 큽니다")

import turtle

t = turtle.pen()

while true:
	direction = input("왼쪽 = left, 오른쪽 = right: ")

	if direction == "l":
		t.left(60)
		t.forward(50)

	if direction == "r":
		t.right(60)
		t.forward(50)


a = 0

while (a < 10):									# 홀 짝 구하기 
	x = int(input("정수를 입력하시오: "))
	if x % 2 == 0:
		print("짝수 입니다.")
	else:
		print("홀수 입니다.")
	a += 1

price = int(input("구입 금액을 입력하시오: "))

if price > 100000:
	dis = price*0.05
	disprice = price - dis
print("지불 할 금액은" ,disprice, "입니다")


a = int(input("이수한 학점수를 입력하시오: "))
b = float(input("평점을 입력하시오: "))

if (a >= 140 and b >= 2.0):
	print("졸업가능")
else:
	print("졸업불가")

import datetime						# 날짜구하기

now = datetime.datetime.now()

print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

if 3 <= now.month <= 5:
	print("이번 달은 {}월로 봄입니다.".format(now.month))
if 6 <= now.month <= 8:
	print("이번 달은 {}월로 여름입니다.".format(now.month))
if 9 <= now.month <= 11:
	print("이번 달은 {}월로 가을입니다.".format(now.month))
if 12 <= now.month <= 2:
	print("이번 달은 {}월로 겨울입니다.".format(now.month)) 