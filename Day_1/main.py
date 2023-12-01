import re
numbers_1 = [] # [ x, x, ...]
numbers_2 = [] # [ x, x, ...]

text_numbers = {"one" :     '1',
                "two" :     '2',
                "three":    '3',
                "four":     '4',
                "five" :    '5',
                "six" :     '6',
                "seven" :   '7',
                "eight" :   '8',
                "nine" :    '9',
                "1":        '1',
                "2":        '2',
                "3":        '3',
                "4":        '4',
                "5":        '5',
                "6":        '6',
                "7":        '7',
                "8":        '8',
                "9":        '9',
                }

def get_numbers(input_string):
    number_lst = []
    for i, value in enumerate(input_string):
        if value.isdigit():
            number_lst.append(value)
    return number_lst

def calc_text_number(input_string : str):
    found = []
    for key,value in text_numbers.items():
        occ = [(m.start(), value) for m in re.finditer(f"{key}", input_string)]
        for x in occ:
            found.append((x[0], x[1]))

    s = sorted(found)
    nums = [x[1] for x in s]

    return nums


def answer_1(content):
    for line in content:
        stripped = line.strip()
        nums = calc_text_number(stripped)
        pair = [nums[0], nums[-1]]
        numbers_1.append(int(f"{pair[0]}{pair[-1]}"))
    return sum(numbers_1)

def answer_2(content):
    for line in content:
        stripped = line.strip()
        nums = get_numbers(stripped)
        pair = [nums[0], nums[-1]]
        numbers_2.append(int(f"{pair[0]}{pair[-1]}"))
    return sum(numbers_2)

if __name__ == "__main__":
    with open("puzzle_input.txt", 'r') as infile:
        content = infile.readlines()
        print("answer star 1:\t", answer_1(content))
        print("answer star 2:\t", answer_2(content))