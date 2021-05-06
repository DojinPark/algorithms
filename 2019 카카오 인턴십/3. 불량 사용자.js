// https://programmers.co.kr/learn/courses/30/lessons/64064
// 3. 불량 사용자
// 걸린 시간: 0:52


function get_banned_set(lists) {
    var banned_set = new Set();
    function dfs(d=0, product=new Set()) {
        if (d == lists.length) {
            let no_repeat = Array.from(product).sort();
            if (no_repeat.length == d) {
                banned_set.add( no_repeat.join(',') );
                return true;
            }
            else
                return false;
        }

        for (let i=0; i<lists[d].length; i++) {
            product.add(lists[d][i]);
            if (product.size == d + 1) {
                dfs(d + 1, product);
                product.delete(lists[d][i]);
            }
        }
    }
    dfs();
    return banned_set;
}

function solution(user_id, banned_id) {
    var answer = 0;
    var N = user_id.length;
    var M = banned_id.length;
    var lists = new Array(M).fill(null).map( () => new Array() );
    
    for (let i=0; i<banned_id.length; i++) {
        let ban = banned_id[i].replace(/\*/g, '.');
        let re = new RegExp(ban);
        for (let user of user_id) {
            if (user.length == ban.length && re.test(user)) {
                lists[i].push(user);
            }
        }
    }

    var banned_set = get_banned_set(lists);

    answer = banned_set.size;

    return answer;
}

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"];
banned_id = ["fr*d*", "abc1**"];
console.log( solution(user_id, banned_id) );