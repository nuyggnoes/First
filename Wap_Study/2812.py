n, k = map(int,input().split())
number = list(input())
stack = []
for i in range(n):
    while k > 0 and stack and stack[-1] < number[i]:
        stack.pop()
        k -= 1
    stack.append(number[i])
print(''.join(stack[:n - k]))