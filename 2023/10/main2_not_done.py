#not completed

def find_junk(used_locations):
    used_locations.sort()
    first_row = used_locations[0][0] +1
    last_row = used_locations[-1][0] -1
    first_pos = min(used_locations, key=lambda sublist: sublist[1])[1] +1
    last_pos = max(used_locations, key=lambda sublist: sublist[1])[1] -1
    counter = 0
    print(f'first row {first_row}, last row {last_row}, first_pos {first_pos}, last_poc {last_pos}')
    for row in range(first_row,last_row):
        for col in range(first_pos,last_pos):
            if [row-1,col-1] in used_locations and [row-1,col] in used_locations and [row-1,col+1] in used_locations and [row,col-1] in used_locations and [row,col+1] in used_locations and [row+1,col-1] in used_locations and [row+1,col] in used_locations and [row+1,col+1] in used_locations:
                
                counter += 1
    print(counter)


def navigation(starting_location,map_translation):
    actual_locations = []
    used_locations = starting_location
    for piece in map_translation:
        if piece[0] == starting_location:
            actual_locations.append([piece[1],piece[2]])
    distance = 1
    used_locations = [starting_location, actual_locations[0][0], actual_locations[0][1], actual_locations[1][0], actual_locations[1][1]]
    print(f'heeeej {used_locations}')
    while True:
        al_hlidac = [0,0]
        for piece in map_translation:
            for i,actual_location in enumerate(actual_locations):
                if actual_location[0] == piece[0] and actual_location[1] == piece[1] and al_hlidac[i] == 0:
                    print(f'Actual location {i} was changed from {actual_location} to {[piece[1],piece[2]]} a hlidac je {al_hlidac}')
                    actual_locations[i] = [piece[1],piece[2]]
                    used_locations.append(piece[2])
                    al_hlidac[i] = 1
                    distance += 1
                    break
        print(f'actual location: {actual_locations}')
        if actual_locations[0][1] == actual_locations[1][1]: # and flag > 20:
            print((distance+3)/2)
            break
    
    used_locations.sort()
    print(f'used location: {used_locations}')
    find_junk(used_locations)

def map(surface):
    translated_map = []
    for row_num, part in enumerate(surface):
        for row_pos, subpart in enumerate(part):
            if subpart == 'S':
                starting_location = [row_num,row_pos]
                print(f'Starting location {starting_location}')
            if subpart == '|':
                translated_map.append([[row_num-1,row_pos],[row_num,row_pos],[row_num+1,row_pos]])
                translated_map.append([[row_num+1,row_pos],[row_num,row_pos],[row_num-1,row_pos]])
            elif subpart == '-':
                translated_map.append([[row_num,row_pos-1],[row_num,row_pos],[row_num,row_pos+1]])
                translated_map.append([[row_num,row_pos+1],[row_num,row_pos],[row_num,row_pos-1]])
            elif subpart == 'L':
                translated_map.append([[row_num-1,row_pos],[row_num,row_pos],[row_num,row_pos+1]])
                translated_map.append([[row_num,row_pos+1],[row_num,row_pos],[row_num-1,row_pos]])
            elif subpart == 'J':
                translated_map.append([[row_num,row_pos-1],[row_num,row_pos],[row_num-1,row_pos]])
                translated_map.append([[row_num-1,row_pos],[row_num,row_pos],[row_num,row_pos-1]])
            elif subpart == '7':
                translated_map.append([[row_num,row_pos-1],[row_num,row_pos],[row_num+1,row_pos]])
                translated_map.append([[row_num+1,row_pos],[row_num,row_pos],[row_num,row_pos-1]])
            elif subpart == 'F':
                translated_map.append([[row_num+1,row_pos],[row_num,row_pos],[row_num,row_pos+1]])
                translated_map.append([[row_num,row_pos+1],[row_num,row_pos],[row_num+1,row_pos]])
    navigation(starting_location,translated_map)

def main():
    with open('input2.txt') as f:
        input = f.read().split('\n')
        map(input)

if __name__ == "__main__":
    main()