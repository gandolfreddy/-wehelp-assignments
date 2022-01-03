function twoSum(nums, target) {
    let iterator = nums.entries();
    for (let item of iterator) {
        let match_num = target - item[1]
        if (nums.includes(match_num))
            return [item[0], nums.indexOf(match_num)]
    }
}


let result = twoSum([2, 11, 7, 15], 9);
console.log(result);