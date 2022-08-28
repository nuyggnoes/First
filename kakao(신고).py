import collections

def solution(id_list, report, k):
    answer = []
    new_list = []
    report = list(set(report))
    for i in range(len(report)):
        report[i] = report[i].split()
    ch = {}
    for i in id_list:
        ch[i] = 0
    for i in range(len(report)):
        ch[report[i][1]] += 1
    for key,value in ch.items():
        if value >= k:
            for i in range(len(report)):
                if key == report[i][1]:
                    new_list.append(report[i][0])
    new_dict = dict(collections.Counter(new_list)) 
    for member in id_list :
        if (member in new_dict.keys()):
            answer.append(new_dict[member])
        else :
            answer.append(0)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))