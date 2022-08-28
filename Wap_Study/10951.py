while True:
    try:                         
        A, B = map(int, input().split())   # A B를 입력 받음
        print(A+B)                         # A+B 출력
    except:
        break                              #입력이 없을 경우 break (예외처리)