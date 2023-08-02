VERSION = 1.0



class PageManager(object):

    ref_counter = 0
    page_frame = None
    page_frame_info = None
    page_replacement_algorithm = "SC"
    # FIFO, LRU, SC(Second Chance)

    def __init__(self, _page_frame_size, _page_replacement_algorithm="SC"):
        self.ref_counter = 0
        self.page_frame = [-1] * _page_frame_size
        self.page_frame_info = [0] * _page_frame_size
        self.page_replacement_algorithm = _page_replacement_algorithm

    def get_curr_page_frame(self):
        return self.page_frame

    def get_curr_page_frame_info(self):
        return self.page_frame_info

    def reference_page(self, _given_page_num):
        is_page_fault = True
        is_page_frame_available = False
        referenced_frame_number = -1

        # 1. check page exists
        for i in range(0, len(self.page_frame)):
            if self.page_frame[i] == _given_page_num:
                referenced_frame_number = i
                
                # i) update frame reference information
                if self.page_replacement_algorithm == "LRU":
                    self.page_frame_info[referenced_frame_number] = self.ref_counter
                elif self.page_replacement_algorithm == "SC":
                    self.page_frame_info[referenced_frame_number] = 1

                is_page_fault = False
                break

        # 2. if page fault occurs, insert or replace page
        if referenced_frame_number == -1:

            # i) check available page exists in the page frame
            for i in range(0, len(self.page_frame)):
                if self.page_frame[i] == -1:        
                    is_page_frame_available = True
                    self.page_frame[i] = _given_page_num
                    if self.page_replacement_algorithm == "FIFO":
                        self.page_frame_info[i] = self.ref_counter
                    elif self.page_replacement_algorithm == "LRU":
                        self.page_frame_info[i] = self.ref_counter
                    elif self.page_replacement_algorithm == "SC":
                        self.page_frame_info[i] = 1
                    break
            # ii) if page frame is not available, replace page
            if not is_page_frame_available:
                referenced_frame_number = self.replace_page(_given_page_num)

        # 3. update timestamp (=ref_counter)
        self.ref_counter += 1

        return [is_page_fault, referenced_frame_number]


    def replace_page(self, _given_page_num):
        replaced_frame_number = -1

        if self.page_replacement_algorithm == "FIFO":
            replaced_frame_number = self.replace_page_with_FIFO(_given_page_num)
        elif self.page_replacement_algorithm == "LRU":
            replaced_frame_number = self.replace_page_with_LRU(_given_page_num)
        elif self.page_replacement_algorithm == "LRU":
            replaced_frame_number = self.replace_page_with_LRU(_given_page_num)
        elif self.page_replacement_algorithm == "SC":
            replaced_frame_number = self.replace_page_with_second_chance(_given_page_num)
        
        return replaced_frame_number


    def replace_page_with_FIFO(self, _given_page_num):
        replaced_frame_number = -1
        # Implement page replacement algorithm with FIFO

        First_In = self.page_frame_info.index(min(self.page_frame_info))    #가장 먼저 들어온 페이지의 인덱스를 First_In 변수에 저장
        self.page_frame[First_In] = _given_page_num                         #page_frame[First_In]에 새로 들어온 페이지 저장
        self.page_frame_info[First_In] = self.ref_counter                   #page_frame_info[First_In]에 새로운 페이지의 들어온 시간(타임스탬프) 저장
        replaced_frame_number = First_In                                    #바뀐 프레임 번호를 반환
        return replaced_frame_number


    def replace_page_with_LRU(self, _given_page_num):
        replaced_frame_number = -1
        # Implement page replacement algorithm with LRU

        First_In = self.page_frame_info.index(min(self.page_frame_info))    #가장 먼저 들어온 페이지의 인덱스를 First_In 변수에 저장
        self.page_frame[First_In] = _given_page_num                         #page_frame[First_In]에 새로 들어온 페이지 저장
        self.page_frame_info[First_In] = self.ref_counter                   #page_frame_info[First_In]에 새로운 페이지의 들어온 시간(타임스탬프) 저장
        replaced_frame_number = First_In                                    #바뀐 프레임 번호를 반환
        return replaced_frame_number                                        #두 코드가 같은 이유는 LRU 알고리즘은 37번째 줄에서 참조할 때 시간을 갱신해 주기 때문에
                                                                            #ref_counter(타임스탬프)값이 가장 작은 페이지프레임을 선택해주면 됨

    def replace_page_with_second_chance(self, _given_page_num):
        replaced_frame_number = -1
        # Implement page replacement algorithm with second chance
        find_frame = False                                          #플래그 생성(참조비트가 0인 곳을 찾았는가)
        while not find_frame :
            for i in range(len(self.page_frame_info)):              #page_frame_info의 길이만큼 반복문 수행
                if self.page_frame_info[i] == 0:                    #참조비트가 0인 경우
                    self.page_frame[i] = _given_page_num            #프레임에 새로운 페이지 번호를 저장
                    replaced_frame_number = i                       #교체된 프레임 번호를 replaced_frame_number에 저장
                    self.page_frame_info[i] = 1                     #참조비트를 1로 수정
                    find_frame = True                               #참조비트 0인 곳을 찾았으므로 플래그 = True
                    break
                else:                                               #참조비트가 1인 경우
                    self.page_frame_info[i] = 0                     #참조비트를 0으로 설정(2차 기회)
        return replaced_frame_number
    
    # def replace_page_with_second_chace(self, _given_page_num):
    #     replaced_frame_number = -1
    #     find_frame = False
    #     while not find_frame:
    #         for i in range(len(self.page_frame_info)):
    #             if self.page_frame_info[i] == 0:
    #                 print("Replaced page")
    #                 replaced_frame_number = i
    #                 self.page_frame_info[i] = i
    #                 self.page_frame = _given_page_num
    #                 find_frame = True
    #                 break
    #             else : 
    #                 print("page fault")
    #                 self.page_frame_info[i] =0
    #     return replaced_frame_number