import process

VERSION = 1.1

def get_process_to_assign_resources(_curr_resource_info, _total_resource_info, _curr_process_waiting_list):
    # Implement deadlock avoidance algorithm based on banker's algorithm
    # If there is no process to pick, return [-1, None]
    # Else, return [1, picked_processes]
    # Where, the picked processes contains list of processes

    picked_processes = []
    is_resource_cannot_be_assigned = False
    available_resources = _curr_resource_info.copy()
    
    # Implement deadlock avoidance algorithm based on banker's algorithm


    if len(_curr_process_waiting_list) > 0:             #자원을 기다리고 있는 프로세스가 있는지 확인
        for process in _curr_process_waiting_list:
            required_resources = process.get_required_resource()

            is_resource_can_be_assigned = True             #프로세스에 필요한 자원을 할당할 수 있는지 확인
            for i in range(len(required_resources)):                
                if required_resources[i] > _total_resource_info[i]:  #요구 자원이 시스템 전체자원보다 클 경우
                    is_resource_cannot_be_assigned = True            #자원할당 불가능
                    break
                elif required_resources[i] > available_resources[i]: #요구 자원이 현재 가용자원보다 클 경우
                    is_resource_can_be_assigned = False              #자원할당 불가능
                    break

            if is_resource_can_be_assigned:             # 모든 요구자원이 할당 가능하면 picked_processes list에 프로세스 추가
                picked_processes.append(process)
                for i in range(len(available_resources)):
                    available_resources[i] -= required_resources[i] #가용 자원에서 차감


    if len(picked_processes) > 0:
        return [1, picked_processes]
    elif is_resource_cannot_be_assigned:
        return [-1, None]
    else:
        return [0, None]