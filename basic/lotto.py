import random
  
gen_count = 5  # 생성할 개수
  
for x in range(0, gen_count):
    arr_selected = random.sample(range(1, 45), 5 )  # 생성
    arr_selected.sort()               # 선택된 번호를 정렬
    print( (' %2d ' * 6) % tuple(arr_selected) )    # 출력
