# 매칭 점수
# https://programmers.co.kr/learn/courses/30/lessons/42893
#
# 풀이 시간 초과
# 노트 1: regex의 기본과 re 라이브러리 사용법
# 노트 2: re 라이브러리의 search나 findall 함수 대신 sub를 이용하여 후처리하면 더 직관적이고 쉽게 풀이할 수 있다.

import re

def __build_page_info(word, page):
    word_regex = r'([^a-z]|\b)' + word + r'([^a-z]|\b)'

    cnt_word = 0
    out_links_cnt = 0
    my_link = ''
    out_links = set()

    # 검색어 매치 개수
        # re.findall() 를 이용한 방법 -> 실패
    # cnt_word = len( re.findall(word_regex, page, re.IGNORECASE) )
        # pattern.search() 를 이용한 방법 -> 실패
    # start = 0
    # pattern = re.compile(word_regex, re.IGNORECASE)
    # while start < len(page):
    #     match = pattern.search(page, start)
    #     if not match: break
    #     cnt_word += 1
    #     start = match.end()
        # split 을 이용한 방법
    cnt_word = re.sub('[^a-z]', ' ', page.lower()).split().count(word.lower())

    print(cnt_word)

    my_link = re.search(r'meta property="og:url" content="(https:\S+)"', page, re.IGNORECASE).group(1)
    
    start = 0
    link_pattern = re.compile(r'a href="(https:\S+)"', re.IGNORECASE)
    while start < len(page):
        match = link_pattern.search(page, start)
        if not match: break

        out_links_cnt += 1
        out_links.add(match.group(1))

        start = match.end()

        # out_links_cnt + len(out_links)
    
    return cnt_word, out_links_cnt, my_link, out_links

def build_info(word, pages):
    word = word.lower()

    info = []
    for page in pages:
        # (word 등장횟수, 외부 링크 등장 횟수, 자신의 링크, 외부 링크 set) 튜플
        info.append(__build_page_info(word, page))
    return info

def build_points(info):
    link_to_idx = {}
    points = []
    
    for i, page in enumerate(info):
        cnt_word, out_links_cnt, my_link, out_links = page
        link_to_idx[my_link] = i
        points.append(cnt_word)
    
    for page in info:
        cnt_word, out_links_cnt, my_link, out_links = page
        if not out_links_cnt: continue
        ext_point = cnt_word / out_links_cnt

        for out_link in out_links:
            if out_link not in link_to_idx.keys(): continue
            
            out_idx = link_to_idx[out_link]
            points[out_idx] += ext_point
    
    return points

def solution(word, pages):
    answer = 0

    # 페이지별  (word 등장횟수, 외부 링크 수, 자신의 링크, 외부 링크 set) 튜플 의 리스트
    info = build_info(word, pages)
    points = build_points(info)
    
    max_point, max_i = 0, 0

    for i, point in enumerate(points):
        if max_point < point:
            max_point = point
            max_i = i
    answer = max_i

    return answer

word = 'blind'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

print( solution(word, pages) )