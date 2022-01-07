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