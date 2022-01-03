function maxZeros(nums) {
    let nums_arr = nums.join('').split('1');
    let nums_len = nums_arr.map(elem => elem.length);
    return Math.max(...nums_len);
}


console.log(maxZeros([0, 1, 0, 0]));
console.log(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]));
console.log(maxZeros([1, 1, 1, 1, 1]));
console.log(maxZeros([0, 0, 0, 1, 1]));