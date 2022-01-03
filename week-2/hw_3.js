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