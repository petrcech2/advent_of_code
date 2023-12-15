import re

def conditions_check(records,groups):
    print(records)
    print(groups)
    for i,record in enumerate(records):
        new_rec = [item for item in record if item]
        print(new_rec)
        for item in new_rec:
            occurrences = item.count('#')
            counter = 0
            for num in groups[i]:
                if int(num) >= occurrences and int(num) <= len(item):
                    counter += 1
            print(counter)


def main():
    with open('input.txt') as f:
        input = f.read().split('\n')
        records,groups = [],[]
        for row in input:
            records.append(re.split(r'\.+', row.split(' ')[0]))
            groups.append(row.split(' ')[1].split(','))
    conditions_check(records,groups)

if __name__ == "__main__":
    main()