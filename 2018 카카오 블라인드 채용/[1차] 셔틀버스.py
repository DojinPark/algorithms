# https://programmers.co.kr/learn/courses/30/lessons/17678
# 정답률:  26.79% (난이도: 중)
# 정확성: 75.0  걸린시간: 01:00
# 정확성: 100.0 걸린시간: 01:00?

START_TIME = 900

def add_time(time, mins):
    h = time // 100
    m = time % 100
    h += (m + mins) // 60
    m = (m + mins) % 60
    return h * 100 + m

def subtract_time(time, mins):
    h = time // 100 - 1
    m = time % 100 + 60
    h += (m - mins) // 60
    m = (m - mins) % 60
    return h * 100 + m

def convert_time(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 100 + m

def revert_time(time):
    h = time // 100
    m = time % 100
    h_str = str(h + 100)[1:]
    m_str = str(m + 100)[1:]
    return h_str + ':' + m_str

def convert_timetable(timetable):
    ret = []
    for time in timetable:
        ret.append( convert_time(time) )
    return ret

def build_bus_timetable(n, t):
    ret = []
    now = START_TIME
    for i in range(n):
        ret.append(now)
        now = add_time(now, t)
        if now > 2359: break
    return ret

def solution(n, t, m, timetable):
    answer = ''

    crew_table = convert_timetable(timetable)
    crew_table.sort()
    bus_table = build_bus_timetable(n, t)

    last_answer = 0
    crew_first_in_line = 0
    for bus in bus_table:
        load = 0
        while load < m:
            if crew_first_in_line < len(crew_table) and crew_table[crew_first_in_line] <= bus:
                crew_first_in_line += 1
                load += 1
            else: break

        # 이번 버스를 타기 위해 다른 크루보다 1분 먼저 도착해야 W하는 경우
        if load == m:
            last_answer = subtract_time(crew_table[crew_first_in_line - 1], 1)
        # 이번 버스를 타기 위해 버스 시간에 맞춰 오면 되는 경우
        else:
            last_answer = bus

    answer = revert_time(last_answer)

    return answer

n = 1;	t = 1;	m = 5;	timetable = ["08:00", "08:01", "08:02", "08:03"]	#09:00
print( solution(n, t, m, timetable) )
n = 2;	t = 10;	m = 2;	timetable = ["09:10", "09:09", "08:00"]	#09:09
print( solution(n, t, m, timetable) )
n = 2;	t = 1;	m = 2;	timetable = ["09:00", "09:00", "09:00", "09:00"]	#08:59
print( solution(n, t, m, timetable) )
n = 1;	t = 1;	m = 5;	timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]	#00:00
print( solution(n, t, m, timetable) )
n = 1;	t = 1;	m = 1;	timetable = ["23:59"]	#09:00
print( solution(n, t, m, timetable) )
n = 10;	t = 60;	m = 45;	timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]	#18:00
print( solution(n, t, m, timetable) )

#09:00
#09:09
#08:59
#00:00
#09:00
#18:00