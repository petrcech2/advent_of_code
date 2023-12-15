with open("input.txt", "r") as file:
    data = file.read().strip()

RECORDS = [
    (x, tuple(map(int, y.split(","))))
    for row in data.split("\n")
    for x, y in [row.split(" ")]
]

print(RECORDS)