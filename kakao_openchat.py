def solution(record):

    answer = []
    dic = { id.split()[1] : id.split()[2] for id in record if id.split()[0] != "Leave"}
    
    for id in record:
        if id.split()[0] == 'Enter':
            answer.append(dic[id.split()[1]] + "님이 들어왔습니다.")
        elif id.split()[0] == 'Leave':
            answer.append(dic[id.split()[1]] + "님이 나갔습니다.")
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))