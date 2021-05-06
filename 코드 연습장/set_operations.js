function isSuperset(set, subset) {
    for (let e of subset) {
        if (!set.has(e)) return false;
    }
    return true;
}

function union(A, B) {
    var ret = new Set(A);
    for (let e of B) {
        ret.add(e);
    }
    return ret;
}

function intersection(A, B) {
    // var ret = new Set(A);
    // for (let e of A) {
    //     if (!B.has(e)) ret.delete(e);
    // }
    // return ret;

    // 더 효율적인 코드
    var ret = new Set();
    for (let e of B) {
        if (A.has(e)) ret.add(e);
    }
    return ret;
}

function symmetricDifference(A, B) { // 합집합 - 교집합
    var ret = new Set(A);
    for (let e of B) {
        if (!A.has(e)) ret.add(e);
        else ret.delete(e);
    }
    return ret;
}

function difference(A, B) {
    var ret = new Set();
    for (let e of A) {
        if (!B.has(e)) ret.add(e);
    }
    return ret;
}

// Examples
const setA = new Set([1, 2, 3, 4])
const setB = new Set([2, 3])
const setC = new Set([3, 4, 5, 6])

console.log(  isSuperset(setA, setB) )          // returns true
console.log()
console.log( union(setA, setC) )               // returns Set {1, 2, 3, 4, 5, 6}
console.log()
console.log( intersection(setA, setC) )        // returns Set {3, 4}
console.log()
console.log( symmetricDifference(setA, setC) ) // returns Set {1, 2, 5, 6}
console.log()
console.log( difference(setA, setC) )          // returns Set {1, 2}