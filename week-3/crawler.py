import csv
from json import loads
from urllib.request import urlopen


url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
data = loads(urlopen(url).read().decode("utf-8"))["result"]["results"]

with open('data.csv', 'w', newline='', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)

    for item in data:
        ## stitle
        stitle = item["stitle"]

        ## region
        address = item["address"]
        region_idx = address.index("區")
        region = address[region_idx-2:region_idx+1]

        ## longitude
        longitude = item["longitude"]

        ## latitude
        latitude = item["latitude"]

        ## file
        file = f"https://{item['file'].split('https://')[1]}"

        writer.writerow([stitle, region, longitude, latitude, file])