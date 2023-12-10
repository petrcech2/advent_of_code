import re

word_to_number={
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


star_sum = 0
with open ('input.csv','r',newline='') as input:
    content = input.read().split('\n')
    for row in content:
        composed_word = ''
        for letter in row:
            composed_word = composed_word+letter
            for key in word_to_number:
                if composed_word.find(key) != -1:
                    composed_word = composed_word.replace(key,word_to_number[key])+key[-1]
        numbers = re.findall(r'\d', composed_word)
        filtered_number = f"{numbers[0]}{numbers[-1]}"
        star_sum=star_sum+int(filtered_number)

print(star_sum)