/* homework 1 */
function calculate(min, max) {
    let sum = 0;
    for (let i = min; i <= max; i++)
        sum += i
    return sum;
}


console.log(calculate(1, 3));
console.log(calculate(4, 8));


/* homework 2 */
function avg(data) {
    let cnt = data["count"];
    let salaries_sum = 0;
    data["employees"].forEach(item => {
        salaries_sum += item["salary"];
    });

    return salaries_sum / cnt;
}


console.log(avg({
    "count": 3,
    "employees": [{
            "name": "John",
            "salary": 30000
        },
        {
            "name": "Bob",
            "salary": 60000
        },
        {
            "name": "Jenny",
            "salary": 50000
        }
    ]
}));


/* homework 3 */
function maxProduct(nums) {
    let product = 1;
    for (let i = 0; i < 2; i++) {
        product *= nums.splice(nums.indexOf(Math.max(...nums)), 1)
    }
    return product
}


console.log(maxProduct([5, 20, 2, 6]));
console.log(maxProduct([10, -20, 0, 3]));
console.log(maxProduct([-1, 2]));
console.log(maxProduct([-1, 0, 2]));


/* homework 4 */
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


/* homework 5 */
function maxZeros(nums) {
    let nums_arr = nums.join('').split('1');
    let nums_len = nums_arr.map(elem => elem.length);
    return Math.max(...nums_len);
}


console.log(maxZeros([0, 1, 0, 0]));
console.log(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]));
console.log(maxZeros([1, 1, 1, 1, 1]));
console.log(maxZeros([0, 0, 0, 1, 1]));