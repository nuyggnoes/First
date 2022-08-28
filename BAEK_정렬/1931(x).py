import sys
n = int(sys.stdin.readline())
st = []
cnt = 0

for _ in range(n):
    t = list(map(int,sys.stdin.readline().split()))
    st.append(t)
st.sort()