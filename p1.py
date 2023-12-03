import re

def read_txt(file_name):
    with open(file_name, 'r') as f:
        for x in f.readlines():
            yield x

def solve1(path):
    def compute_line(line):
        digits = [x for x in line if x.isnumeric()]
        return int(f"{digits[0]}{digits[-1]}")
    
    sum = 0
    for line in read_txt(path):
        sum += compute_line(line)
    return sum

# print(solve1("inputs/1.txt"))

def solve2(path):
    def compute_line(line):
        mapping = dict(
            zero='0',
            one='1',
            two='2',
            three='3',
            four='4',
            five='5',
            six='6',
            seven='7',
            eight='8',
            nine='9'
        )
        occurrences = dict()
        for key,_ in mapping.items():
            occurrences[key]=[m.start() for m in re.finditer(key, line)]
        min_index = 100
        min_value = None
        max_index = -1
        max_value = None
        for key, vals in occurrences.items():
            if vals:
                if min(vals) < min_index:
                    min_index = min(vals)
                    min_value = key
                if max(vals) > max_index:
                    max_index = max(vals)
                    max_value = key
        if min_value:
            line = line.replace(min_value, mapping[min_value], 1)
        if max_value:
            line = line.replace(max_value, mapping[max_value], 1)
        digits = [x for x in line if x.isnumeric()]
        return int(f"{digits[0]}{digits[-1]}")
    
    sum = 0
    for line in read_txt(path):
        # print(line, compute_line(line))
        sum += compute_line(line)
    return sum
print(solve2("inputs/2.txt"))