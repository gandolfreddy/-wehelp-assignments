function calculate(min, max) {
    let sum = 0;
    for (let i = min; i <= max; i++)
        sum += i
    return sum;
}


console.log(calculate(1, 3));
console.log(calculate(4, 8));