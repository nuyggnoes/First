import sys

n = int(sys.stdin.readline())
tree_list = {}

for i in range(n):
    tree = sys.stdin.readline().rstrip()
    if tree not in tree_list:
        tree_list[tree] = 1
    else:
        tree_list[tree] += 1

for name in sorted(tree_list.keys()):
    print(name, '%.4f' % (tree_list[name]*100 / n))