def seeds_sum(seeds):
    origin_seeds = seeds[::2]
    seeds_addition = seeds[1::2]
    new_seed_list = []
    for i in range(len(origin_seeds)):
        new_seed_list.append([int(origin_seeds[i]),int(origin_seeds[i])+int(seeds_addition[i])-1])
    return new_seed_list

def mergeIntervals(intervals):
    for item in intervals:
        item.sort()

    intervals.sort()
    stack = []
    stack.append(intervals[0])
    for i in intervals[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
 
    return intervals

def counter(mapping,seeds):
    if not mapping:
        return seeds
    else:
        new_seed_list = []
        for seed in seeds:
            changed = False
            for item in mapping:
                flag = ''
                destination_num = int(item[0])
                source_num = int(item[1])
                range_len = int(item[2])
                if int(source_num) <= int(seed[0]) < int(source_num)+range_len:
                    flag = 'L'
                if int(source_num) <= int(seed[1]) < int(source_num)+range_len:
                    if flag == '':
                        flag = 'R'
                    else: flag = 'B'
                if changed!= True:
                    if flag == 'L':
                        new_seed_list.append([int(seed[0]) + int(destination_num) - int(source_num), int(destination_num) + range_len -1 ])
                        seed[0] = int(source_num) + range_len
                        seeds.append(seed)
                        changed = True
                    elif flag == 'R':
                        new_seed_list.append([int(destination_num), int(seed[1]) - int(source_num) + int(destination_num)])
                        seed[1] = int(source_num) - 1
                        seeds.append(seed)
                        changed = True
                    elif flag == 'B':
                        new_seed_list.append([int(seed[0]) - int(source_num) + int(destination_num), int(seed[1]) - int(source_num) + int(destination_num)])
                        changed = True
            
            if changed == False:
                new_seed_list.append(seed)
        merged_list = mergeIntervals(new_seed_list)
        return merged_list



def main():
    with open('input2.txt') as f:
        input = f.read().split('\n')
        last_line = input[-1]
        mapping = []
        for row in input:
            if row.strip():
                if row.find('seeds') != -1:
                    seeds = seeds_sum(row.split(': ')[1].split(' '))
                elif row.find('map') != -1:
                    seeds = counter(mapping,seeds)
                    mapping = []
                elif str(row)[0].isnumeric():
                    mapping.append(row.split(' '))
                
                if row==last_line:
                    seeds = counter(mapping,seeds)
        print(seeds[0][0])

if __name__ == "__main__":
    main()