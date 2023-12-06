def counter(mapping,seeds):
    print(f'running encounter: {mapping}')
    if not mapping:
        return seeds
    else:
        flag_list = [None] * len(seeds)
        for item in mapping:
            destination_num = int(item[0])
            source_num = int(item[1])
            range_len = int(item[2])
            for seed_position, seed in enumerate(seeds):
                if int(source_num) <= int(seed) < int(source_num)+range_len and flag_list[seed_position] != 'CH':
                    print(f"Seed je: {seed}, source_num je {source_num} a destination_num je {destination_num}")
                    seeds[seed_position] = int(seed) - int(source_num) + int(destination_num)
                    flag_list[seed_position] = 'CH' 
        print(f"Seeds = {seeds}")
        return seeds



def main():
    with open('input.txt') as f:
        input = f.read().split('\n')
        last_line = input[-1]
        mapping = []
        for row in input:
            if row.strip():
                #print(f"Row: {row}")
                if row.find('seeds') != -1:
                    seeds = row.split(': ')[1].split(' ')
                elif row.find('map') != -1:
                    seeds = counter(mapping,seeds)
                    mapping = []
                elif str(row)[0].isnumeric():
                    mapping.append(row.split(' '))
                
                if row==last_line:
                    seeds = counter(mapping,seeds)
        print(seeds)
        seeds.sort()
        print(seeds[0])

if __name__ == "__main__":
    main()