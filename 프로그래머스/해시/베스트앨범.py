# https://programmers.co.kr/learn/courses/30/lessons/42579
# 베스트앨범
# 걸린 시간: 0:21

def solution(genres, plays):
    answer = []
    N = len(plays)

    gen_cnt = {}
    songs_by_gen = {}
    
    for i in range(N):
        gen = genres[i]

        if gen not in gen_cnt.keys():
            gen_cnt[gen] = 0
        gen_cnt[gen] += plays[i]

        if gen not in songs_by_gen.keys():
            songs_by_gen[gen] = []
        songs_by_gen[gen].append( (-plays[i], i) )

    for _, gen in sorted( [ (v, k) for k, v in gen_cnt.items()], reverse = True ):
        songs_by_gen[gen].sort()
        if len(songs_by_gen[gen]) == 1:
            answer.append( songs_by_gen[gen][0][1] )
        else:
            answer += [songs_by_gen[gen][0][1], songs_by_gen[gen][1][1]]

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]	
print( solution(genres, plays) ) # [4, 1, 3, 0]