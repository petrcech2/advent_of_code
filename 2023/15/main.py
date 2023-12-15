def hash_counter(input):
    cnt = 0
    for item in input:
        current_value = 0
        for char in item:
            current_value += ord(char)
            current_value = current_value*17%256
        cnt += current_value
    print(cnt)

def main():
    with open('input.txt') as f:
        input = f.read().split(',')
        hash_counter(input)
if __name__ == "__main__":
    main()