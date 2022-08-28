import re
def solution(new_id):
    answer = ''
    answer = new_id.lower()  #step.1
    answer = re.sub('[^a-z-_\.0-9]', '', answer)  #step.2
    answer = re.sub('\.+', '.', answer)   #step.3
    answer = re.sub('^[.]|[.]$', '', answer)  #step.4
    answer = 'a' if len(answer) == 0 else answer[:15]  #step.5&6
    answer = re.sub('^[.]|[.]$', '', answer)   #step.6
    answer = answer if len(answer) > 2 else answer + "".join(answer[-1] for i in range(3-len(answer)))   #step.7
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))
