# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
# 7. 추석 트래픽
# 정답률 17.99% (난이도: 상)
# 걸린시간 01:00
#
# 슬라이딩 윈도우 사용은 함정.
# 내 풀이는 투포인터 응용.
# 1. 각 작업의 시작시간, 끝시간을 다른 어레이에 저장한 후 각자 정렬.
# 2. 시작시간에 대한 루프를 돌리면서, 동시 처리량을 하나씩 더해줌
# 3.     지금 시작시간 빼기 1초(초당처리시간을 구해야 하므로) 보다 시간값이 작은 끝시간 개수 만큼 동시 처리량을 빼줌. 이 때, 마지막으로 확인한 끝시간에 포인터가 머물러 있음.
# 시간 복잡도는 정렬 부분 O(N lgN), 투포인터 부분 O(2N)

SECOND = 1000

def get_ms_duration(duration):
    duration = duration[:-1]
    s_float = float(duration)
    return int(s_float * 1000)

def get_ms_endtime(hms):
    h, m, s = hms.split(':')
    s, ms = s.split('.')
    h_ms = int(h) * 3600000 # 60 분 * 60 초 * 1000 ms
    m_ms = int(m) * 60000   # 60 초 * 1000 ms
    s_ms = int(s) * 1000    # 1000 ms
    ms = int(ms)
    return h_ms + m_ms + s_ms + ms

def solution(lines):
    answer = 0

    starts = []
    ends = []

    for line in lines:
        day, endtime, duration = line.split()
        endtime_ms = get_ms_endtime(endtime) - 1
        duration_ms = get_ms_duration(duration) - 1
        starts.append(endtime_ms - duration_ms)
        ends.append(endtime_ms)

    starts.sort()
    ends.sort()    

    throughput = 0
    last_end = -1
    for start in starts:
        throughput += 1
        for i in range(last_end + 1, len(ends)):
            if ends[i] <= start - SECOND:
                throughput -= 1
                last_end = i
            else: break
        answer = max(answer, throughput)
    return answer

lines = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]
print( solution(lines) )
# 1

lines = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]
print( solution(lines) )
# 2

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
print( solution(lines) )
# 7