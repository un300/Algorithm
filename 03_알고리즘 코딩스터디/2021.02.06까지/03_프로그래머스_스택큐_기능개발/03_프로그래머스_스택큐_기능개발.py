from collections import deque

def solution(progress_list, speed_list):

    answer = []

    progress_queue = deque(progress_list)
    speed_queue = deque(speed_list)
    while progress_queue:
        progress_queue = deque([progress + speed for progress, speed in zip(progress_queue, speed_queue) ])

        cnt = 0
        for progress in progress_queue:
            if progress >= 100 :
                cnt += 1
            else :
                break
        if cnt != 0:
            answer.append(cnt)

        for _ in range(cnt):
            progress_queue.popleft()
            speed_queue.popleft()

    return answer