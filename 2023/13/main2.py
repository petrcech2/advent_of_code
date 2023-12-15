#not working

def find_duplicate_rows(input_str,flag):
    print('find duplicates was called')
    for row in input_str:
        print(row)
    out_num = 0
    for i in range(0,len(input_str)-3):
        print('\n')
        rows_to_compare = [input_str[i+1],input_str[i]]
        print(f'{rows_to_compare} and position {i} a and string length = {len(input_str)}')
        for j in range(i+2,i+3):
            print(f'to compare {input_str[j:j+len(rows_to_compare)]}')
            if input_str[j:j+len(rows_to_compare)] == rows_to_compare:
                if flag == 'r':
                    out_num = (i+2)*100
                elif flag == 'c':
                    out_num = i+2
    return out_num

            
def convert_columns(input_str):
    new_list = []
    for i in range(len(input_str[0])):
        str = ''
        for row in input_str:
            str += row[i]
        new_list.append(str)
    return find_duplicate_rows(new_list,'c')


def main():
    with open('input.txt') as f:
        input_data = f.read()
        input_list = [block.split('\n') for block in input_data.split('\n\n') if block]
        cnt,tmp = 0,0
        for object in input_list:
            tmp = convert_columns(object)
            if tmp > 0:
                cnt += tmp
            else:
                 cnt += find_duplicate_rows(object,'r')
            print(cnt)

if __name__ == "__main__":
    main()