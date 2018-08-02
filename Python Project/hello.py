import fstring

print("swati")

a = 6
b = 3
c = a + b
print(c)
d = a * b
print(d)
e = a - b
print(e)
f = a / b
print(f)
g = a % b
print(g)
h = a ** b
print(h)
i = a + b * c
print(i)
j = (a + b) * (c + d)
print(j)
a = 'fshshj'
print(a)
a = a + a
print(a)

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)
print('hi \n I am late')
print('hi\thello')
p = len("I am swati")
print(p)

string = "Bangalore Karnataka"
newstring = string[-11]
print(newstring)
y = string.split('a')
print(y)
name = 'Swati '
h = name[2:]  # type: str
print(h)

q = "I"
r = "am"
s = "\nSwati"
print(q, r, s)

l = "w" + h * 10 + " " * 10
print(l)

pop = 'z' * 10
print(pop)

v = '2' + '3'
print(v)

print("This is a string{}{}".format(' inserted', ' new '))

result = 111.111
test = 999.9997
# print(result)
print('This is a result {1:15.3f} is right'.format(result, test))

lista = (1, 2, 3)
lista = (1.4, 'string')
print(len(lista))
print(lista)
print(type(lista))
print(id(lista))

print("-----------------")
lista = (1, 2, 3)
lista = (1.4, 'string')
print(len(lista))
print(lista)
print(type(lista))
print(id(lista))

lista = [1, 2, 3]
lista = [1.4, 'string']
print(len(lista))
print(lista)
print(type(lista))
print(id(lista))

print("-----------------")
lista = [1, 2, 3]
lista = [1.4, 'string']
print(len(lista))
print(lista)
print(type(lista))
print(id(lista))

mylist = [1, 2, 3]
mylist = ['one', 'three']
new_list = lista + mylist
print(new_list)

mylist[0] = 0
print(mylist)

mylist.append('two')
print(mylist)
print(mylist.pop())
print(mylist)

print(mylist.pop())
print(mylist)

sortlist = [9, 3, 5, 1, 6, 0]
sortlist.sort()
print(sortlist)
print(type(sortlist))
res = sortlist.reverse()
print(res)

my_dict = {'language1': 'java', 'language2': 'C'}
print(my_dict)
print(my_dict['language1'])

versions = {'java': '3.2', 'C': '4.4'}
print(versions['java'])

d = {'k1': '123', 'k2': [1, 2, 3], 'k3': {'insidekey': '100'}}
print(d['k2'][1])

d = {'k1': ['a', 'b', 'c']}
nlist = d['k1']
print(nlist)
letter = nlist[1].upper()
# up =letter.upper()
# print(up)
print(letter)
d = {'k1': '100', 'k2': '200'}
d['k3'] = 300
print(d)
d['k1'] = 'NEW VALUE'
print(d)
print(d.keys())
print(d.values())
print(d.items())

# t = ('one',3)
# t[1]
# print(t[1])

l = [1, 2, 3]
print(l[-1])
type(l)
print(type(l))
l[0] = 'new'
print(l)

t = ('a', 'a', 'b')

print(t.count('a'))

print(t.index('a'))
myset = set()
myset.add(5)
myset.add(2)
print(myset)
melist = [1, 1, 1, 7, 7, 6, 6]
print(set(melist))

people = set('Jay')
people.add('Daxit')
people.add('mit')
print(people)

qw = 1
qe = 2
ad = qw > qe
print(ad)

b = none
print(b)

f = open('F://file.txt')
f.write('Python')
