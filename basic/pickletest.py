import pickle
data={1:'python',2:'you'}
f= open('test_p.txt','wb')
pickle.dump(data,f)
#파일로저장할때 사용 /dumps파이썬안에서 피클객체로쓸때
f.close()

f=open('test_p.txt','rb')
data1=pickle.load(f)
f.close()

print(data)
print(data1)
print(type(data1))