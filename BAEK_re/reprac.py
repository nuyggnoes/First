import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    sum = 0
    score = 1
    quiz_result = input().rstrip()
    for i in quiz_result:
        if i == 'O':
            sum += score
            score += 1
        elif i == 'X':
            score = 1
    print(sum)
