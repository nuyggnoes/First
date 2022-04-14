import sys

n = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
number_list = list(map(int,sys.stdin.readline().split()))

for i in number_list:
    if i in number:
        print(1)
    else:
        print(0)