# https://programmers.co.kr/learn/courses/30/lessons/17680
# 3. 캐시
# 정답률: 45.26% (난이도: 하)
# 걸린시간: 0:16
#
# CS 지식인 LRU 구현법을 아는지 묻는 문제
# 캐시 사이즈가 0인 경우 예외 처리

from collections import deque

def solution(cacheSize, cities):
    answer = 0

    cache_size = cacheSize

    cities = [city.lower() for city in cities]
    cache = deque()

    for city in cities:
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if cache_size:
                if len(cache) == cache_size:
                    cache.popleft()
                cache.append(city)

    return answer



cache_size = 3;	cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']	#50
print( solution(cache_size, cities) )
cache_size = 3;	cities = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']	#21
print( solution(cache_size, cities) )
cache_size = 2;	cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']	#60
print( solution(cache_size, cities) )
cache_size = 5;	cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']	#52
print( solution(cache_size, cities) )
cache_size = 2;	cities = ['Jeju', 'Pangyo', 'NewYork', 'newyork']	#16
print( solution(cache_size, cities) )
cache_size = 0;	cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']	#25
print( solution(cache_size, cities) )