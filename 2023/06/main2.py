import re

def win_counter(time, distance):
    win_cnt = 0
    for i in range(time+1):
        speed = i
        if (time-i)*speed > distance:
            win_cnt+=1
    return win_cnt


def main():
    with open('input.txt') as f:
        input = f.read().split('\n')
        number = int("".join(input[0].split()).split(':')[1])
        distance = int("".join(input[1].split()).split(':')[1])
        print(win_counter(number,distance))
if __name__ == "__main__":
    main()