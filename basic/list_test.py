a=[]
b=[1,2,3]
c=['life', 'is']
d=[1,2,'life']
e=[1,2,[1,2,3]]


print(a)
print(b)
print(c)
print(d)
print(e[2][1])

print(type(a))

a=[1,2,3]
a[2]=4
print(a)

del a[1]#문자열삭제
print (a)
a.append(0)
print(a)

a=[5,4,6,6,8,7]
z= a.index(5)
print(z)

dic={1:10,2:{20}}#{20}은 set이라고 부름
print(dic.keys())#키값만 출력
print(dic.items())
print(dic.values())
print(dic.clear())

