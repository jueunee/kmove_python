money = True
if money:
    print("택시")
else:
    pass#쓸게없을때 씀
print("walk")    

score = int(input("성적을 입력하시오\n"))
print('입력한 성적은 %s 이다.' %score)

if score >= 90:
    total = 'A'
elif score>=80:
    total = 'B'
elif score>=60:
    total = 'C'
elif score>=50:
    total = 'D'   
else:
    total = 'F'

print('당신의 학점은 {}입니다'.format(total))