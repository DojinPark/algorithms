#include <iostream>

#include <string>
#include <vector>
#include <algorithm>
#define INF 0x7FFFFFFF

using namespace std;

int solution(vector<int> food_times, long long k) {
    int answer = 0;
    int total_t = 0;

    for (int i=0; i<food_times.size(); i++) {
        total_t += food_times[i];
    }
    if (total_t <= k) return -1;
    
    while (true) {
        int L = 0;
        int min_t = INF;
        for (int i=0; i<food_times.size(); i++) {
            if (food_times[i]) {
                L++;
                min_t = min(min_t, food_times[i]);
            }            
        }
        
        int sub = 1;
        if (k >= L * min_t) sub = min_t;
        
        for (int i=0; i<food_times.size(); i++) {
            if (k == 0) return i+1;
            if (food_times[i]) {
                food_times[i] -= sub;
                k -= sub;           
            }

        }
    }
    
    return answer;
}

int main() {
    vector<int> food_times = {3, 1, 2};
    int k = 5;
    cout << solution(food_times, k) << endl;


}