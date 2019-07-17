import random
  
list = []
ran_num = random.randint(1,45)  
for i in range(5):
    while ran_num in list:
        ran_num = random.randint(1,45) 
    list.append(ran_num)
    
list.sort()         
print(list)   

