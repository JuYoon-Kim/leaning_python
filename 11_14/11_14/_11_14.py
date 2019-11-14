import turtle

p = turtle.Turtle()

num_sides = int(input("숫자를 입력하시오: "))
side_length = 70
angle = 360.0/num_sides

for i in range(num_sides):
	p.forward(side_length)
	p.right(angle)

i = 0;					# break도 잘 됨

while i <10:

	print(i)
	i += 1
	if i == 3:
		break

dan = int(input("단을 입력하시오: "))

for i in range(1,10):
	print(dan, '*', i, '=' ,dan*i)

sum = 0
for i in range(3,101,3):
	sum += i
print(sum)

list1 = []
for i in range (1,101):
	list1.append(i)

# list1.append("a")     문자를 넣었기 때문에 type에러가 뜬다
print(list1)     

print(sum(list1))