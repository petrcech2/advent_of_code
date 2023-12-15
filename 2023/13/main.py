def row_or_col(i,flag):
    if flag == 'r':
        return (i+1)*100
    elif flag == 'c':
        return i+1

def find_duplicate_rows(input_str,flag):
    out_num = 0
    for i in range(0,len(input_str)-1):
        if input_str[i] == input_str[i+1]:
            if i+1 > len(input_str)/2:
                if input_str[(i+1)*2-len(input_str):i+1] == input_str[-1:-len(input_str)+i:-1]:
                    out_num = row_or_col(i,flag)
            else:
                reversed_list = [item for item in reversed(input_str[i+1:(i+1)*2])]
                if input_str[:i+1] == reversed_list:
                    out_num = row_or_col(i,flag)
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
        cnt = 0
        for object in input_list:
            cnt += convert_columns(object)
            cnt += find_duplicate_rows(object,'r')
    print(cnt)

if __name__ == "__main__":
    main()