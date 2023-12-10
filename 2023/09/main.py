import re


def osi_sensor(report):
    result = report[-1]
    count = 0
    helper = [report]
    while True:
        tmp = [helper[-1][i + 1] - helper[-1][i] for i in range(len(helper[-1]) - 1)]
        helper.append(tmp)
        count += 1
        if tmp.count(0) == len(tmp):
            break
    result += sum(helper[-i][-1] for i in range(1, len(helper)) if helper[-i])
    return(result)

def main():
    with open('input.txt') as f:
        input = f.read().split('\n')
        result = sum(osi_sensor(row) for row in [list(map(int, re.findall(r'-?\d+', row))) for row in input])
        print(result)

if __name__ == "__main__":
    main()