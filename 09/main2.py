import re


def osi_sensor(report):
    count = 0
    helper = [report]
    while True:
        tmp = [helper[-1][i + 1] - helper[-1][i] for i in range(len(helper[-1]) - 1)]
        helper.append(tmp)
        count += 1
        if tmp.count(0) == len(tmp):
            break
    result = helper[len(helper)-2][0]
    for i in range(3,count+2):
        result = helper[len(helper)-i][0] - result
    return(result)

def main():
    with open('input.txt') as f:
        input = f.read().split('\n')
        result = sum(osi_sensor(row) for row in [list(map(int, re.findall(r'-?\d+', row))) for row in input])
        print(result)

if __name__ == "__main__":
    main()