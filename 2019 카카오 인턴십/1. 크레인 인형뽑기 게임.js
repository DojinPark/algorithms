// https://programmers.co.kr/learn/courses/30/lessons/64061
// 1. 크레인 인형뽑기 게임

function solution(board, moves) {
    var answer = 0;
    var N = board.length;
    var lines = Array(N).fill().map(() => Array())
    var stack = Array();

    for (let c = 0; c < N; c++) {
        for (let r = N - 1; r >= 0; r--) {
            if (board[r][c] > 0)
                lines[c].push( board[r][c] );
            else break;
        }
    }

    for (let m of moves) {
        m -= 1;
        if (lines[m].length > 0) { 
            stack.push( lines[m].pop() )
            if (stack.length >= 2 && stack[stack.length - 1] == stack[stack.length - 2]) {
                answer += 2;
                stack.pop();
                stack.pop();
            }
        }
    }

    return answer;
}

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
console.log( solution(board, moves) )