#랜덤초이스, 5개반복 ,while문으로 같을때까지 계속반복, 몇초만에맞췄는지
import random
import time
word = ["zoo","yellow","purple","안흥팥찐빵","gallery"]
num= 1
g = random.choice(word)
input()
start = time.time()
print(word)

while num<=5:
    print("Quiz",num )
    print(g)
    user= input()
    if g == user:
        print("ok")
        num= num+1
        g= random.choice(word)
    else:
        print("again")
        
end = time.time()
r=end-start
print("경과시간:",r,"초")