import random

num = random.sample(range(1,10),3)
print(num)
strike =0 
ball=0
count =0
while(strike <3):
    num1 = input("숫자를 입력하세요: ")

    if(num1[0]==num1[1]==num1[2]):
        count +=1
        continue
    elif(num1[0]==num1[1]):
        count +=1
        continue
    elif(num1[0]==num1[2]):
        count +=1
        continue
    elif(num1[1]==num1[2]):
        count +=1
        continue
    else:
        pass

    for i in range(0,3):
        for j in range(0,3):
            if(num1[i]==str(num[j])and i==j):
                strike +=1
            elif(num1[i]==str(num[j])and i!=j):
                ball+=1

    print(strike,"스트라이크",ball,"볼")
    count+=1

print( count,"번 만에 맞췄습니다" )
            