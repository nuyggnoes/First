a=[]
count=1
for i in range(10):
    n = int(input())  # int형으로 n에 저장
    n %= 42  # 42로 나눈 나머지를 다시 n에 저장 후
    a.append(n)  # 리스트 a에 바로 추가
b=set(a)  # 중복 제거
print(len(b))