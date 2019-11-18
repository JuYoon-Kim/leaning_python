
def get_sum(start,end):
	sum = 0
	for i in range(start,end+1):
		sum += i 
	return sum

value = get_sum(1,10)
print(value)

def asterisk_test(a,b,*args):
	return a + b + sum(args)

print(asterisk_test(1,2,3,4,5))

a = input("문자열을 입력하시오: ")
alp,dit,spa = 0,0,0


for i in a:
	if i.isalpha():
		alp = alp + 1
	elif i.isdigit():
		dit = dit + 1
	elif i.isspace():
		spa = spa + 1

print("알파벳 문자의 개수 =",alp)
print("숫자 문자의 개수 =",dit)
print("스페이스 문자의 개수 =",spa)