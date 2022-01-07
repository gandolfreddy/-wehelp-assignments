function twoSum(nums, target) {
    /*
    Time Complexity:
        O(twoSum(nums, target)): 
            O(n) + O(n)*(O(1))+O(n)) + O(1)+O(n)*O(n) => O(n^2) in average-case.

    reference: 
        1. https://tc39.es/ecma262/#sec-array.prototype.entries
        2. https://tc39.es/ecma262/#sec-array.prototype.includes
        3. https://tc39.es/ecma262/#sec-array.prototype.indexof
    */

    // array.prototype.entries(): O(n) in average-case
    let iterator = nums.entries();

    // for loop iteration: O(n) in this case
    for (let item of iterator) {
        // one statement: O(1) in average-case
        let match_num = target - item[1]

        // array.prototype.includes(): O(n) in average-case 
        if (nums.includes(match_num))
        // array.prototype.indexof(): O(n) in average-case 
            return [item[0], nums.indexOf(match_num)]
    }
}


let result = twoSum([2, 11, 7, 15], 9);
console.log(result);