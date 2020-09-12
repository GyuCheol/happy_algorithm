/**
 * Map 사용 문제
 * Javascript는 별도의 자료구조를 제공하지 않는다는 점을 배움..
 * Heap, queue, hash map 등,
 * object를 map처럼 사용할 순 있으나,,,
 */

function solution(participant, completion) {
    var participant_map = {};
    var completion_map = {};

    participant.forEach(key => {
        if (key in participant_map) {
            ++participant_map[key];
        } else {
            participant_map[key] = 0;
        }
    });

    completion.forEach(key => {
        if (key in completion_map) {
            ++completion_map[key];
        } else {
            completion_map[key] = 0;
        }
    });

    participant.forEach(key => {
        if (!(key in completion_map) || participant_map[key] != completion_map[key]) {
            return key
        }
    });

}

console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
console.log(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
console.log(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
