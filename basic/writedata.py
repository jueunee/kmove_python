
f= open('basic/rank.txt','w',encoding='utf8')



f.close()
'''
f= open('basic/tast.txt','r',encoding='utf8')
line = f.readline().replace('\n','')
print(line,end='')
print(type(line))
f.close()

f= open('basic/tast.txt','r',encoding='utf8')
line = f.readlines()
print(line,end='')
print(type(line))

for i in line:
    print(i.replace('\n',''))

f.close()
'''
f = open("basic/tast.txt",'a',encoding='utf8')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()