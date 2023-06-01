
def get_process_idx_from_queue(_curr_process, _process_ready_queue, _scheduling_algorithm, _curr_process_run_tick=-1, _time_quantum=-1):
    selected_idx = -1

    if _scheduling_algorithm == "FCFS":
        selected_idx = first_come_first_served(_curr_process, _process_ready_queue)
    elif _scheduling_algorithm == "RR":
        selected_idx = round_robin(_curr_process, _process_ready_queue, _curr_process_run_tick, _time_quantum)
    elif _scheduling_algorithm == "SJF":
        selected_idx = shortest_job_first(_curr_process, _process_ready_queue)
    elif _scheduling_algorithm == "SRJF":
        selected_idx = shortest_remaining_job_first(_curr_process, _process_ready_queue)

    return selected_idx



def first_come_first_served(_curr_process, _process_ready_queue):
    selected_idx = -1
    # Select process to run
    if _curr_process is None and len(_process_ready_queue) > 0 :    #현재 실행 중인 프로세스가 없고, 준비 큐에 프로세스가 대기중이면
        selected_idx = 0                                            #첫 번째 프로세스 선택
    return selected_idx


def round_robin(_curr_process, _process_ready_queue, _curr_process_run_tick = -1, _time_quantum = -1):
    selected_idx = -1
    # Select process to run
    if _curr_process is not None and _curr_process_run_tick >= 0 :  #현재 실행 중인 프로세스가 있는 경우
        if _curr_process_run_tick == _time_quantum :                #현재 실행 중인 프로세스 run_tick이 시간 할당량과 같으면
            _process_ready_queue.append(_curr_process)              #실행 중인 프로세스를 준비 큐에 추가
            _curr_process_run_tick = 0                              #run_tick을 0으로 초기화
        else :
            selected_idx = -1                                       #현재 실행 중인 프로세스를 계속 실행
    
    if selected_idx == -1:                                          #현재 실행 중인 프로세스가 없거나 시간 할당량을 초과한 경우
        if len(_process_ready_queue) > 0:                           #준비 큐에서 다음 실행할 프로세스를 선택
            selected_idx = 0

    return selected_idx


def shortest_job_first(_curr_process, _process_ready_queue):
    selected_idx = -1
    # Select process to run
    min_time = 11                                            #실행시간은 최대 10
    
    if _curr_process is None:                                #실행 중인 프로세스가 없을 경우
        for i,process in enumerate(_process_ready_queue):    #준비 큐를 순환하면서
            if process.req_run_time < min_time:              #가장 짧은 실행시간 선택
                selected_idx = i
                min_time = process.req_run_time

    return selected_idx


def shortest_remaining_job_first(_curr_process, _process_ready_queue):
    selected_idx = -1
    # Select process to run
    min_remaining_time = 11                                                #실행시간은 최대 10

    if _curr_process is not None and _curr_process.get_remaining_time() < min_remaining_time:  #현재 실행중인 프로세스의 잔여시간을 확인
        min_remaining_time = _curr_process.get_remaining_time()
        selected_idx = -1

    for idx, process in enumerate(_process_ready_queue):                #준비 큐를 순환하여
        if process.get_remaining_time() < min_remaining_time:           
            min_remaining_time = process.get_remaining_time()           #가장 작은 잔여 시간을 min_remaining_time에 저장
            selected_idx = idx                                          #그에 해당하는 인덱스를 selected_idx에 저장

    return selected_idx