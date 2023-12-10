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
        time = [int(item) for item in re.findall(r'\d+', input[0])]
        distance = [int(item) for item in re.findall(r'\d+', input[1])]
        possibilities = 1
        for i in range(len(time)):
            possibilities = possibilities * win_counter(time[i],distance[i])
        print(possibilities)
if __name__ == "__main__":
    main()