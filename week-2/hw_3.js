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
    let len = nums.length;
    q_sort(nums, 0, len);
    let product_1 = nums[len - 1] * nums[len - 2];
    let product_2 = (nums[0] * nums[1] === -0) ? 0 : nums[0] * nums[1];
    return Math.max(product_1, product_2);
}


console.log(maxProduct([5, 20, 2, 6]));
console.log(maxProduct([10, -20, 0, 3]));
console.log(maxProduct([-1, 2]));
console.log(maxProduct([-1, 0, 2]));
console.log(maxProduct([-1, -2, 0]));