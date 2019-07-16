money = True
if money:
    print("택시")
else:
    pass#쓸게없을때 씀
print("walk")    

score = input("성적을 입력하시오\n")
print('입력한 성적은 %s 이다.' %score)
if int(score) > 90:
    print('A')
elif int(score)>80:
    print('B')
elif int(score)>60:
    print('C')
elif int(score)>50:
    print('D')    
else:
    print('F')