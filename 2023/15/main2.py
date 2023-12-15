import re

def counter(input):
    cnt = 0
    for key in input:
        for i,item in enumerate(input[key]):
            focal_length = re.search(r'\d+', item)
            cnt += (key+1) * (i+1) * int(focal_length.group())
    print(cnt)

def hashmap(input):
    boxes = {key: [] for key in range(256)}
    for item in input: 
        current_value = 0
        item_substr =  re.sub(r'[^a-zA-Z]', '', item)
        if '=' in item:
            for char in item_substr:
                current_value += ord(char)
                current_value = current_value*17%256
            position = [index for index, tmp in enumerate(boxes[current_value]) if item_substr in tmp]
            if not position:
                boxes[current_value].append(item)
            else:
                boxes[current_value][position[0]] = item
        elif '-' in item:
            for key, box_items in boxes.items():
                box_items[:] = [box_item for box_item in box_items if item_substr != re.sub(r'[^a-zA-Z]', '', box_item)]
    counter(boxes)

def main():
    with open('input.txt') as f:
        input = f.read().split(',')
        hashmap(input)
if __name__ == "__main__":
    main()