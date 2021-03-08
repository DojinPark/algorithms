# https://programmers.co.kr/learn/courses/30/lessons/42893
# 매칭 점수 (2019 카카오 블라인드 채용)
# 걸린 시간: 1:01
#
# 노트: ex) <a href="https://a.com" attribute="value"/>
#      - url 찾는 과정에서 패턴을 r'href="(.*)"' 으로 하면
#        https://a.com" attribute="value 가 검색됨
#      - r'href="(\S*)"'으로 해야
#        https://a.com 이 검색됨

import re
def solution(word, pages):
    N = len(pages)

    # 소문자 처리
    word = word.lower()
    pages = [page.lower() for page in pages]

    # 기본점수
    base_scores = [0] * N
    for i, page in enumerate(pages):
        words = re.split('[^a-z]', page)
        base_scores[i] = words.count(word)
    # print(base_scores)

    # 해당 페이지 링크
    link_to_indices = {}
    for i, page in enumerate(pages):
        link = re.search(r'<meta.*og:url.*"https://(\S*)"', page).group(1)
        link_to_indices[link] = i
    # print(link_to_indices)

    # 외부 링크 점수
    ext_links = [ [] for _ in range(N) ]
    ext_scores = [0] * N
    pat = re.compile(r'<a href="https://(\S*)"')
    for i, page in enumerate(pages):
        start = 0
        while start < len(page):
            match = pat.search(page, start)
            if not match: break
            ext_links[i].append(match.group(1))
            start = match.end()
    ext_scores = [ base_scores[i] / len(ext_links[i]) if ext_links[i] else 0 for i in range(N) ]
    # print(ext_links)
    # print(ext_scores)

    # 합산점수
    for i in range(N):
        for ext_link in ext_links[i]:
            if ext_link not in link_to_indices.keys(): continue

            ext_i = link_to_indices[ext_link]
            base_scores[ext_i] += ext_scores[i]

    result = sorted( [(-score, i) for i, score in enumerate(base_scores)] )

    return result[0][1]

word = 'blind'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print( solution(word, pages) ) # 0

word = 'Muzi'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print( solution(word, pages) ) # 1