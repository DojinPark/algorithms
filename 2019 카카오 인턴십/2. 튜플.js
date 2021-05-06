// https://programmers.co.kr/learn/courses/30/lessons/64065
// 2. 튜플

function solution(s) {
    var answer = [];
    var tuples = new Array();
    // var re = /'{(\S)}'/g;
    var re = new RegExp('{([^{}]+)}', 'g');
    
    while (m = re.exec(s)) {
        console.log(m[1])
        tuples.push(m[1].split(',').map(x => parseInt(x)));
    }

    console.log(tuples)
    tuples.sort( (a, b) => a.length - b.length )
    console.log(tuples)

    console.log([1,2,3,4].sort((a, b) => a - b))

    return answer;
}

s = "{{2},{2,1,3,4},{2,1},{2,1,3}}"
console.log( solution(s) );

// console.log( '1,2,3,4'.split(',').map(x => parseInt(x)) )
