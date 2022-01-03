def avg(data):
    cnt = data["count"]
    salaries_sum = sum([item["salary"] for item in data["employees"]])

    return salaries_sum/cnt

    
print(avg({
    "count": 3,
    "employees": [
        {
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
}))
