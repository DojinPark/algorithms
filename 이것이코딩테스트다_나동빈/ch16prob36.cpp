# 편집 거리
# 책 문제와는 다른
# https://www.acmicpc.net/problem/7620
# 으로 대체

#define INF 1000000000
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    string str1, str2;
    cin >> str1;
    cin >> str2;

    int len1 = str1.length();
    int len2 = str2.length();

    str1.insert(0, " ");
    str2.insert(0, " ");

    vector< tuple< int, vector< tuple<char, char> > > > dp[2];
    bool sel = true;

    for(int i1 = 1; i1 < len1; i1++) {
        vector< tuple
        dp[sel][i1] = [
    }

for i1 in range(1, len1 + 1):
    dp[sel][i1] = [ i1, [('d', str1[i]) for i in range(1, i1 + 1)] ]

for i2 in range(1, len2 + 1):
    sel = not sel
    dp[sel][0] = [ i2, [('a', str2[i]) for i in range(1, i2 + 1)] ]
    for i1 in range(1, len1 + 1):
        min_cost, min_steps = INF, []
        if str1[i1] == str2[i2]:
            cost, steps = dp[not sel][i1 - 1]
            min_cost, min_steps = cost, steps + [('c', str1[i1])]
        else:
            cost, steps = dp[sel][i1 - 1]
            if cost + 1 < min_cost:
                min_cost = cost + 1
                min_steps = steps + [('d', str1[i1])]

            cost, steps = dp[not sel][i1 - 1]
            if cost + 1 < min_cost:
                min_cost = cost + 1
                min_steps = steps + [('m', str2[i2])]

            cost, steps = dp[not sel][i1]
            if cost + 1 < min_cost:
                min_cost = cost + 1
                min_steps = steps + [('a', str2[i2])]
            
        dp[sel][i1] = [min_cost, min_steps]

answer_steps = dp[not sel][len1][1]
for step in answer_steps:
    command, character = step
    print(command, character)

}
