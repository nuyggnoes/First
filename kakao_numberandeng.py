def solution(s):
    answer = 0
    ans = ''
    eng = ''
    st = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in s:
        if i.isdigit(): ans += i
        else:
            eng += i
            for i in range(len(st)):
                if eng == st[i]:
                    ans += str(i)
                    eng = ''
    answer = int(ans)
    return answer
s = "123"
print(solution(s))