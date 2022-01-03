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