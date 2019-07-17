import time
count=0
input("엔터를 누르면 시작됩니다")
t= time.time()
input("20초후에 다시 엔터를 누릅니다.")
t2 = time.time()
d=t2-t

print("실제시간 : %d 초" %d )
print("차이 :", abs(d-20),"초" )

