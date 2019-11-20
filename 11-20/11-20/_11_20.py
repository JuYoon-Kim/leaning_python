
num ={2,1,3}

for x in num:
	print(x,end="",)
for j in num:
	print(j,end="")
for k in num:
	print(k,end="")

s = 'Never put off till tomorrow what you can do today.'
print(s.split())
print(s.isalpha())
print(s.isdigit())
print(s.upper())
print(s.lower())
print(s.replace('put','off'))
print(s.startswith('Never'))

a = input()
b = len(a)
c = ''

for i in range(b - 1, -1, -1):
	c = c + a[i]

if c == a :
	print("회문 입니다.")
else:
	print("회문이 아닙니다.")

class Counter:
	def reset(self):
		self.count = 0
	def incr(self):
		self.count += 1
	def get(self):
		return self.count

a = Counter()
a.reset()

for i in range(5):
	a.incr()

print(a.get())	