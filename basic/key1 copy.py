#랜덤초이스, 5개반복 ,while문으로 같을때까지 계속반복, 몇초만에맞췄는지
import random
import time
word = ["zoo","yellow","purple","안흥팥찐빵","gallery"]
rank= {}
n= 1
def sortV(x):
    return x[1]
    

while True:
    print("1.문제불러오기 2.타자게임 3.등수목록 4.저장 5.불러오기" )
    menu= input("메뉴를 선택하세요\n")

    if menu=='1':
        f=open('basic/word.txt','r',encoding='utf8')
        line=1
        word.clear()
        while line:
            line = f.readline().replace("\n","")
            if not(line==''):
                word.append(line)
        print(word)
            

    elif menu=='2':
        n=1
        print("타자게임 준비되면 엔터")
        input()
        start = time.time()
        q=random.choice(word)
        while n<=5:
            print("문제",n)
            print(q)
            x=input()
            if q==x:
                print("pass")
                n=n+1
                q=random.choice(word)
            else:
                print("오타! 다시도전")
        end= time.time()
        et=end-start
        et=format(et,".2f")
        print("타자시간",et,"초")
        name = input("사용자 이름을 입력하세요")
        rank[name]=float(et)
    elif menu=='3':
        
        ranklist=sorted(rank.items(),key=sortV)
        print(type(ranklist))
        num=1
        for k,v in ranklist:
            print("%d등 %s %f" %(num,k,v))
            num=num+1
    elif menu=='4':
        f=open('basic/rank.txt','w',encoding='utf8')
        text=''
        items = rank.items()
        for k,v in items:
            text=text+k+':' + str(v)+'\n'
        f.writelines(text)
        f.close()
    elif menu=='5':
        f=open('basic/rank.txt','r')
        line=1
        while line:
            line= f.readline().replace("\n","")
            if not(line==''):
                k,v=line.split(':')
                rank[k]=float(v)
    else:
        pass
            
