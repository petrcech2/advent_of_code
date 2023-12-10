def navigation(starting_location,map_translation):
    actual_locations = []
    for piece in map_translation:
        if piece[0] == starting_location:
            actual_locations.append([piece[1],piece[2]])
    distance = 1
    #print(actual_locations)
    while True:
        al_hlidac = [0,0]
        for piece in map_translation:
            for i,actual_location in enumerate(actual_locations):
                if actual_location[0] == piece[0] and actual_location[1] == piece[1] and al_hlidac[i] == 0:
                    print(f'Actual location {i} was changed from {actual_location} to {[piece[1],piece[2]]} a hlidac je {al_hlidac}')
                    actual_locations[i] = [piece[1],piece[2]]
                    al_hlidac[i] = 1
                    distance += 1
                    break
        print(f'actual location: {actual_locations}')
        flag += 1
        if actual_locations[0][1] == actual_locations[1][1]: # or flag > 20:
            print((distance+3)/2)
            break

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
    with open('input.txt') as f:
        input = f.read().split('\n')
        map(input)

if __name__ == "__main__":
    main()