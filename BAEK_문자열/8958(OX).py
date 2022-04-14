import sys

def one_to_n(x):
    sum = 0
    for i in range(1,x+1):
        sum += i
    return sum

for _ in range(int(sys.stdin.readline())):
    ox = sys.stdin.readline().rstrip()
    ox_list = ox.split('X')
    score = 0
    for i in ox_list:
        score += one_to_n(len(i))
    print(score)
