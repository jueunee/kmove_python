import random,time

count=0 #맞힌개수 파악
oper=['+','-','*','//']

input("게임시작")#시작시간체크
t= time.time()

for x in range(0,5):#문제출제시점
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    op = random.choice(oper)

    quiz=str(a)+op+str(b)
    quiz='%d %s %d'%(a,op,b)
    
    print(quiz,'=')#문제출제
    print(eval(quiz))#퀴즈문자열 결과 출력
    c=int(input('정답='))#정답 입력받음

    if int(eval(quiz))==c:
        print("정답!")
        count+=1
    else:
        print("오답!")

t2 = time.time() 
d=t2-t      
print("%.0f 초동안 %d개 맞음" %(d,count))

