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
function swap(data, i, j) {
    let temp = data[i];
    data[i] = data[j];
    data[j] = temp;
}


function q_sort(data, left, right) {
    if (left < right) {
        let pivot = data[left];
        let i = left,
            j = right;

        while (i < j) {
            do i++; while (i < right && data[i] < pivot);
            do j--; while (j >= left && data[j] > pivot);

            if (i < j) swap(data, i, j);
        }

        swap(data, left, j);
        q_sort(data, left, j);
        q_sort(data, j + 1, right);
    }
}


function maxProduct(nums) {
    /*
    Time Complexity:
        O(maxProduct(nums)): 
            O(1) + O(1) + O(nlogn) + O(1) + O(n) => O(nlogn) in best-case and average-case.
            O(1) + O(1) +  O(n^2)  + O(1) + O(n) => O(n^2) in worst-case.
    
    reference:
        1. https://tc39.es/ecma262/#sec-properties-of-array-instances-length
        2. https://tc39.es/ecma262/#sec-math.max
    */
    // one statement: O(1) in average-case.
    let left = 0;
    // array.prototype.length: O(1) in average-case.
    let right = len = nums.length;

    // quick sort algorithm:
    //    O(nlogn) in best-case and average-case.
    //    O(n^2) in worst-case.
    q_sort(nums, left, right);

    // two statements: O(1) in average-case.
    let product_1 = nums[len - 1] * nums[len - 2];
    let product_2 = (nums[0] * nums[1] === -0) ? 0 : nums[0] * nums[1];

    // Math.max(): O(n) in average-case.
    return Math.max(product_1, product_2);
}


console.log(maxProduct([5, 20, 2, 6]));
console.log(maxProduct([10, -20, 0, 3]));
console.log(maxProduct([-1, 2]));
console.log(maxProduct([-1, 0, 2]));
console.log(maxProduct([-1, -2, 0]));


/* homework 4 */
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


/* homework 5 */
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