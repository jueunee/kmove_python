listdata=[]
while True:
    print('''
    ===============리스트 데이터 관리 ==========
    1.리스트에 추가 2. 리스트 데이터 수정 
    3. 리스트 데이터 삭제 4.종료

    ''')
    menu = int(input("메뉴를 선택하시오"))
    if menu == 4:
       break
    elif menu == 1:
        data=input("추가할 데이터를 입력하세요")
        listdata.append(data)
        print(listdata)
    elif menu ==2:
        data=int(input("몇번째 데이터를 수정하세요?"))
        while data > len(listdata):
            data=int(input("다시입력"))
            data2=input("수정할 데이터를 입력하세요")     
            listdata[data-1]=data2
        print(listdata)
        print("완료")
    elif menu ==3:
        data = int(input("몇번째 데이터를 삭제하세요?"))
        while data > len(listdata):
            data=int(input("다시입력"))
            del listdata[data-1] 
        print(listdata)
        print("완료")
    else:
        print("메뉴를 다시선택해주세요")