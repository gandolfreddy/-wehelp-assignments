function maxZeros(nums) {
    /*
    Time Complexity:
        O(maxZeros(nums)): 
            O(n) + O(n) + O(n)*O(1) + O(n) => O(n) in average-case.

    reference: 
        1. https://tc39.es/ecma262/#sec-array.prototype.join
        2. https://tc39.es/ecma262/#sec-string.prototype.split
        3. https://tc39.es/ecma262/#sec-array.prototype.map
        4. https://tc39.es/ecma262/#sec-math.max
    */

    // Array.prototype.join(): O(n) in average-case.
    // String.prototype.split(): O(n) in average-case.
    let nums_arr = nums.join('').split('1');

    // Array.prototype.map(): O(n) in average-case.
    // Array.prototype.length: O(1) in average-case.
    let nums_len = nums_arr.map(elem => elem.length);

    // Math.max(): O(n) in average-case.
    return Math.max(...nums_len);
}


console.log(maxZeros([0, 1, 0, 0]));
console.log(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]));
console.log(maxZeros([1, 1, 1, 1, 1]));
console.log(maxZeros([0, 0, 0, 1, 1]));